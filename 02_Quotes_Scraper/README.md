# Quotes Scraper & Multi-Format Exporter

A Python web scraper built to extract quotes, authors, and category tags from quotes.toscrape.com and export structured data into standard CSV, JSON, and styled Excel spreadsheets.

## Key Features
- **Data Extraction:** Scrapes quote text, author names, and category tags.
- **Multi-Format Export:**
  - `quotes.csv` – Standard CSV file for database ingestion.
  - `quotes.json` – Clean JSON structure for API/web consumption.
  - `quotes.xlsx` – Professionally formatted Excel file featuring dark blue headers, auto-adjusted column widths, wrapped text, and centered alignment.

## Tech Stack
- **Python 3.x**
- **Requests** (HTTP client)
- **BeautifulSoup4** (HTML parsing)
- **OpenPyXL** (Excel formatting)

## How to Run
```bash
python scraper.py
```