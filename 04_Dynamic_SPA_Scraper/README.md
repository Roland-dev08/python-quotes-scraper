# Dynamic SPA Web Scraper (Playwright)

A robust Python web scraper built with Playwright designed to extract dynamic, JavaScript-rendered data across multiple pages of a Single Page Application (SPA) and export it into production-ready formats (CSV, JSON, Excel).

## Key Features

- **Dynamic SPA Scraping**: Automates a headless Chromium browser to handle client-side rendered dynamic JavaScript content.
- **Asynchronous Execution**: Leverages `asyncio` and `playwright.async_api` for fast, efficient execution.
- **Multi-Format Export**:
  - `quotes_dynamic.csv` – Clean data standard for database import.
  - `quotes_dynamic.json` – Structured JSON for API integration.
  - `quotes_dynamic.xlsx` – Professionally styled Excel spreadsheet.

## 🛠️ Tech Stack & Libraries

- **Python 3.x**
- **Playwright**
- **Pandas**
- **OpenPyXL**

## Output Data Structure

| Field | Type | Example |
| :--- | :--- | :--- |
| **quote** | String | The world as we have created it is a process of our thinking. |
| **author** | String | Albert Einstein |
| **tags** | String | change, deep-thoughts, thinking |

## How to Run

```bash
python scraper.py
```