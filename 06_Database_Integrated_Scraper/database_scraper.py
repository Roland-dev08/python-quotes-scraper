import sqlite3
import logging
import json
import re
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("database_scraper.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DatabaseIntegratedScraper:
    """
    Automated Web Scraper with direct SQLite Database Integration, 
    data cleaning, deduplication, and multi-format exports.
    """
    
    BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
    DB_NAME = "scraped_books.db"

    def __init__(self, max_pages: int = 5):
        self.max_pages = max_pages
        self.scraped_data: List[Dict[str, Any]] = []
        self._setup_database()

    def _setup_database(self) -> None:
        """Initializes SQLite database and creates target schema table if not exists."""
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT UNIQUE NOT NULL,
                    price_gbp REAL NOT NULL,
                    rating INTEGER NOT NULL,
                    availability TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            logger.info(f"Database setup complete. Connected to '{self.DB_NAME}'.")

    def _convert_rating(self, rating_class: str) -> int:
        """Converts text-based star rating class to integer (1-5)."""
        ratings_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        for key, value in ratings_map.items():
            if key in rating_class:
                return value
        return 0

    def parse_page(self, html_content: str) -> List[Dict[str, Any]]:
        """Parses raw HTML and extracts structured book attributes."""
        soup = BeautifulSoup(html_content, "html.parser")
        products = soup.select(".product_pod")
        page_items = []

        for prod in products:
            title_el = prod.select_one("h3 a")
            price_el = prod.select_one(".price_color")
            rating_el = prod.select_one(".star-rating")
            avail_el = prod.select_one(".availability")

            title = title_el.get("title", "").strip() if title_el else ""
            raw_price = price_el.text.strip() if price_el else "0.0"
            price = float(re.sub(r"[^\d.]", "", raw_price)) if raw_price else 0.0
            
            rating_str = rating_el.get("class", []) if rating_el else []
            rating = self._convert_rating(" ".join(rating_str))
            
            availability = avail_el.text.strip() if avail_el else "Unknown"

            page_items.append({
                "title": title,
                "price_gbp": price,
                "rating": rating,
                "availability": availability
            })
        
        return page_items

    def save_to_database(self, items: List[Dict[str, Any]]) -> None:
        """Inserts records into SQLite database with duplication prevention."""
        inserted_count = 0
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            for item in items:
                try:
                    cursor.execute("""
                        INSERT INTO books (title, price_gbp, rating, availability)
                        VALUES (?, ?, ?, ?)
                        ON CONFLICT(title) DO UPDATE SET
                            price_gbp = excluded.price_gbp,
                            rating = excluded.rating,
                            availability = excluded.availability
                    """, (item["title"], item["price_gbp"], item["rating"], item["availability"]))
                    inserted_count += 1
                except sqlite3.Error as e:
                    logger.error(f"Failed to insert record '{item.get('title')}': {e}")
            conn.commit()
        logger.info(f"Database transaction complete. Upserted {inserted_count} records.")

    def run(self) -> None:
        """Main execution flow across targeted catalog pages."""
        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

        for page in range(1, self.max_pages + 1):
            url = self.BASE_URL.format(page)
            logger.info(f"Fetching Page {page}: {url}")
            try:
                response = session.get(url, timeout=10)
                response.raise_for_status()
                items = self.parse_page(response.text)
                self.scraped_data.extend(items)
                logger.info(f"Successfully scraped {len(items)} items from Page {page}.")
            except requests.RequestException as e:
                logger.error(f"HTTP request failed for {url}: {e}")

        # Store into Database
        if self.scraped_data:
            self.save_to_database(self.scraped_data)

    def export_data(self) -> None:
        """Queries SQLite database to generate verified CSV, JSON, and XLSX files."""
        with sqlite3.connect(self.DB_NAME) as conn:
            df = pd.read_sql_query("SELECT id, title, price_gbp, rating, availability, created_at FROM books", conn)

        if df.empty:
            logger.warning("No records found in database to export.")
            return

        # Export CSV
        df.to_csv("books_database.csv", index=False, encoding="utf-8-sig")

        # Export JSON
        df.to_json("books_database.json", orient="records", indent=4, force_ascii=False)

        # Export Excel
        df.to_excel("books_database.xlsx", index=False)

        logger.info(f"Successfully exported {len(df)} database records to CSV, JSON, and XLSX.")

if __name__ == "__main__":
    scraper = DatabaseIntegratedScraper(max_pages=5)
    scraper.run()
    scraper.export_data()