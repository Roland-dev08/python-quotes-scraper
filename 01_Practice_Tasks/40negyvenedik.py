import requests
from bs4 import BeautifulSoup
import csv
import re
import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("cli_projekt.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def ar_tisztitas(nyers_ar):
    talalat = re.search(r"[\d.]+", nyers_ar)
    return float(talalat.group()) if talalat else 0.0

def profi_cli_scraper(max_ar, kimeneti_fajl):
    logging.info(f"CLI Scraper indítása | Szűrés: max {max_ar} GBP | Kimenet: {kimeneti_fajl}")
    url = "https://books.toscrape.com/"

    fejlec = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    try:
        valasz = requests.get(url, headers=fejlec, timeout=10)
        soup = BeautifulSoup(valasz.text, "html.parser")

        konyvek = []
        for termek in soup.select("article.product_pod"):
            cím = termek.h3.a["title"]
            nyers_ar = termek.select_one("p.price_color").text
            ar = ar_tisztitas(nyers_ar)

            if ar <= max_ar:
                konyvek.append({
                    "Cím": cím,
                    "Ár (GBP)": ar
                })

        with open(kimeneti_fajl, "w", newline="", encoding="utf_8_sig") as f:
            writer = csv.DictWriter(f, fieldnames=["Cím", "Ár (GBP)",], delimiter=";")
            writer.writeheader()
            writer.writerows(konyvek)

        logging.info(f"Siker! {len(konyvek)} könyv kiírva a(z) '{kimeneti_fajl}' fájlba.")

    except Exception as e:
        logging.error(f"Hiba történt: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Profi Megrendelői Scraper CLI Eszköz")
    parser.add_argument("--max-ar", type=float, default=25.0, help="Maximum könyvtár GBP-ben")
    parser.add_argument("--kimenet", type=str, default="cli_konyvek.csv", help="Kimeneti CSV fájl neve")

    args = parser.parse_args()
    profi_cli_scraper(args.max_ar, args.kimenet)