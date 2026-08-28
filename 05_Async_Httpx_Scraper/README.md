# High-Speed Asynchronous Web Scraper (HTTPX & asyncio)

A high-performance Python web scraper built with **HTTPX** and **asyncio** designed to fetch and process dynamic API endpoints concurrently with rate limiting and multi-format data exports.

## Key Features

- **Asynchronous Concurrency**: Executes multiple HTTP requests simultaneously using `httpx.AsyncClient` and `asyncio.gather` for maximum speed.
- **Concurrency Control**: Implements `asyncio.Semaphore` to limit concurrent connections and prevent IP rate-limiting.
- **Multi-Format Export**:
  - `quotes_async.csv` – Clean CSV export for database loading.
  - `quotes_async.json` – Structured JSON format for REST APIs.
  - `quotes_async.xlsx` – Styled spreadsheet for reporting.
- **Logging**: Full execution tracking via standard Python logging to `async_scraper.log`.

## 🛠️ Tech Stack & Libraries

- **Python 3.x**
- **HTTPX** (Asynchronous HTTP client)
- **asyncio** (Asynchronous I/O framework)
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
python async_scraper.py
```