import asyncio
import logging
import json
import pandas as pd
from typing import List, Dict, Any
from playwright.async_api import async_playwright, Page, BrowserContext

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("scraper.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DynamicSPAScraper:
    """
    Asynchronous Web Scraper for dynamic Single Page Applications using Playwright.
    """
    
    BASE_URL = "https://quotes.toscrape.com/js/"

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.extracted_data: List[Dict[str, Any]] = []

    async def extract_page_data(self, page: Page) -> List[Dict[str, Any]]:
        """Extracts dynamic quote elements from the rendered DOM."""
        await page.wait_for_selector(".quote")
        quotes = await page.query_selector_all(".quote")
        page_items = []

        for quote in quotes:
            text_el = await quote.query_selector(".text")
            author_el = await quote.query_selector(".author")
            tag_els = await quote.query_selector_all(".tags .tag")

            text = await text_el.inner_text() if text_el else ""
            author = await author_el.inner_text() if author_el else ""
            tags = [await tag.inner_text() for tag in tag_els]

            page_items.append({
                "quote": text.strip("“”"),
                "author": author.strip(),
                "tags": ", ".join(tags)
            })
        
        return page_items

    async def run(self) -> None:
        """Main execution flow for crawling dynamic pages."""
        async with async_playwright() as p:
            logger.info("Launching headless Chromium browser...")
            browser = await p.chromium.launch(headless=self.headless)
            context: BrowserContext = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page: Page = await context.new_page()

            current_url = self.BASE_URL
            page_number = 1

            while current_url:
                logger.info(f"Navigating to Page {page_number}: {current_url}")
                try:
                    await page.goto(current_url, wait_until="networkidle", timeout=30000)
                    items = await self.extract_page_data(page)
                    self.extracted_data.extend(items)
                    logger.info(f"Successfully scraped {len(items)} items from Page {page_number}.")

                    # Handle dynamic pagination
                    next_button = await page.query_selector(".pager .next a")
                    if next_button:
                        href = await next_button.get_attribute("href")
                        current_url = f"https://quotes.toscrape.com{href}" if href else None
                        page_number += 1
                    else:
                        logger.info("No further pages found. Dynamic pagination complete.")
                        current_url = None

                except Exception as e:
                    logger.error(f"Error scraping {current_url}: {e}", exc_info=True)
                    break

            await browser.close()
            logger.info("Browser session closed.")

    def export_data(self) -> None:
        """Exports extracted data into JSON, CSV, and Excel formats."""
        if not self.extracted_data:
            logger.warning("No data available to export.")
            return

        df = pd.DataFrame(self.extracted_data)

        # JSON Export
        with open("quotes_dynamic.json", "w", encoding="utf-8") as f:
            json.dump(self.extracted_data, f, ensure_ascii=False, indent=4)
        
        # CSV Export
        df.to_csv("quotes_dynamic.csv", index=False, encoding="utf-8-sig")

        # Excel Export
        df.to_excel("quotes_dynamic.xlsx", index=False)

        logger.info(f"Successfully exported {len(df)} total records to JSON, CSV, and XLSX.")

async def main():
    scraper = DynamicSPAScraper(headless=True)
    await scraper.run()
    scraper.export_data()

if __name__ == "__main__":
    asyncio.run(main())