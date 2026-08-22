# Multi-Page E-Commerce Product Scraper

A robust Python scraper designed to extract structured product data across multiple pages of an e-commerce catalogue and export it into production-ready formats (**CSV, JSON, and custom-styled Excel**).

## Key Features
- **Multi-Page Pagination:** Automatically navigates through multiple catalogue pages.
- **Data Extraction:** Extracts Product ID, Title, Price, Numeric Star Rating (1-5), Stock Availability, and Direct Links.
- **Multi-Format Export:**
  - `products.csv` – Clean data standard for database import.
  - `products.json` – Structured JSON for API integration.
  - `products.xlsx` – Professionally styled spreadsheet featuring dark blue headers, wrapped text, auto-adjusted column widths, and proper cell alignment.

## 🛠️ Tech Stack & Libraries
- **Python 3.x**
- **Requests**
- **BeautifulSoup4**
- **OpenPyXL**

## Output Data Structure

| Field | Type | Example |
| :--- | :--- | :--- |
| **ID** | Integer | `1` |
| **Title** | String | `A Light in the Attic` |
| **Price (£)** | Float | `51.77` |
| **Rating** | Integer | `3` |
| **Availability** | String | `In stock` |
| **URL** | String | `http://books.toscrape.com/...` |

## How to Run
```bash
python ecommerce_scraper.py
```