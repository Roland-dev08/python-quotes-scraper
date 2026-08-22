# Python Quotes Scraper & Data Exporter

A Python web scraper built with `requests`, `BeautifulSoup4`, and `openpyxl` to extract quotes, authors, and tags from quotes.toscrape.com, with multi-format data export capabilities.

## Features
- Extracts quote text, author names, and category tags
- Auto-exports raw data to **CSV** (`quotes.csv`) and **JSON** (`quotes.json`)
- Generates a fully styled **Excel spreadsheet** (`quotes.xlsx`) featuring:
  - Custom dark blue headers with white text
  - Automatic column auto-sizing and text wrapping
  - Pre-configured landscape layout for seamless PDF conversion

## Tech Stack
- Python 3
- `requests`
- `beautifulsoup4`
- `openpyxl`

## How to Run
1. Install required dependencies:
   ```bash
   pip install requests beautifulsoup4 openpyxl
```
