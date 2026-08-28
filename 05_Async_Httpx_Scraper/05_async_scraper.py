import asyncio
import json
import logging
from typing import Any, Dict, List
import httpx
import pandas as pd

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("async_scraper.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AsyncHttpxScraper:
    """
    High-performance asynchronous web scraper leveraging httpx and asyncio
    with concurrency limits (Semaphore) and multi-format data export.
    """
    BASE_URL = "https://quotes.toscrape.com/api/quotes"
    MAX_CONCURRENCY = 5  # Limits concurrent connections to prevent IP blocks

    def __init__(self, total_pages: int = 10):
        self.total_pages = total_pages
        self.semaphore = asyncio.Semaphore(self.MAX_CONCURRENCY)
        self.results: List[Dict[str, Any]] = []

    async def fetch_page(self, client: httpx.AsyncClient, page: int) -> List[Dict[str, Any]]:
        """Fetches a single API page asynchronously with concurrency control."""
        async with self.semaphore:
            url = f"{self.BASE_URL}?page={page}"
            logger.info(f"Fetching Page {page}: {url}")
            try:
                response = await client.get(url, timeout=10.0)
                response.raise_for_status()
                data = response.json()
                
                page_items = []
                for item in data.get("quotes", []):
                    page_items.append({
                        "quote": item.get("text", "").strip("“”"),
                        "author": item.get("author", {}).get("name", "").strip(),
                        "tags": ", ".join(item.get("tags", []))
                    })
                logger.info(f"Successfully processed Page {page} ({len(page_items)} quotes).")
                return page_items
            except Exception as e:
                logger.error(f"Error fetching Page {page}: {e}")
                return []

    async def run(self) -> None:
        """Executes concurrent requests across all target pages using asyncio.gather."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        async with httpx.AsyncClient(headers=headers, follow_redirects=True) as client:
            tasks = [self.fetch_page(client, page) for page in range(1, self.total_pages + 1)]
            pages_data = await asyncio.gather(*tasks)
            
            for items in pages_data:
                self.results.extend(items)
            
        logger.info(f"Asynchronous scraping complete. Total records collected: {len(self.results)}")

    def export_data(self) -> None:
        """Exports extracted data into JSON, CSV, and Excel formats."""
        if not self.results:
            logger.warning("No data extracted to export.")
            return

        df = pd.DataFrame(self.results)

        # CSV Export
        df.to_csv("quotes_async.csv", index=False, encoding="utf-8-sig")
        
        # JSON Export
        with open("quotes_async.json", "w", encoding="utf-8") as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)

        # Excel Export
        df.to_excel("quotes_async.xlsx", index=False)

        logger.info("Successfully exported data to CSV, JSON, and XLSX formats.")

async def main():
    scraper = AsyncHttpxScraper(total_pages=10)
    await scraper.run()
    scraper.export_data()

if __name__ == "__main__":
    asyncio.run(main())