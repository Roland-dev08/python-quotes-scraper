# Database Integrated Web Scraper (SQLite & Python)

A production-ready web scraper built with Python, **Requests**, **BeautifulSoup4**, and **SQLite** designed to scrape web data, persist it into a relational database with conflict resolution (upsert), and export clean datasets into multiple formats.

## Key Features

- **Relational Database Storage**: Integrates directly with an **SQLite3** database for structured data persistence.
- **Data Deduplication & Upsert**: Uses `ON CONFLICT` SQL logic to prevent duplicate entries and keep product records updated.
- **Robust Parsing & Cleaning**: Cleans raw currency symbols, parses star ratings into integers, and normalizes text fields.
- **Multi-Format Export**: Queries SQLite directly to generate verified output files:
  - `books_database.csv` – Standard CSV for analysis.
  - `books_database.json` – Structured JSON output.
  - `books_database.xlsx` – Styled Excel spreadsheet.
- **Logging**: Comprehensive logging recorded in `database_scraper.log`.

## 🛠️ Tech Stack & Libraries

- **Python 3.x**
- **SQLite3** (Relational Database)
- **Requests & BeautifulSoup4**
- **Pandas**
- **OpenPyXL**

## Database Schema (`books` table)

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| **id** | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique record ID |
| **title** | TEXT | UNIQUE, NOT NULL | Book title |
| **price_gbp** | REAL | NOT NULL | Price cleaned to numerical float |
| **rating** | INTEGER | NOT NULL | Star rating integer (1-5) |
| **availability** | TEXT | NOT NULL | Stock status |
| **created_at** | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Insert timestamp |

## How to Run

```bash
python database_scraper.py
```