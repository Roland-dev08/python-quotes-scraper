import requests
from bs4 import BeautifulSoup
import csv
import re
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("kaparas.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def ar_tisztitas(nyers_ar):
    talalat = re.search(r"[\d.]+", nyers_ar)
    return float(talalat.group()) if talalat else 0.0

def szurt_export_scraper(max_ar=30.0):
    logging.info(f"Adatgyűjtés indítása (Szűrés: max {max_ar} GBP)...")
    url = "https://books.toscrape.com/"

    try:
        valasz = requests.get(url, timeout=10)
        soup = BeautifulSoup(valasz.text, "html.parser")

        szurt_konyvek = []

        for termek in soup.select("article.product_pod"):
            nyers_cim = termek.h3.a["title"]
            nyers_ar = termek.select_one("p.price_color").text
            nyers_keszlet = termek.select_one("p.instock.availability").text.strip()

            ar = ar_tisztitas(nyers_ar)
            van_raktaron = "In stock" in nyers_keszlet

            if ar <= max_ar and van_raktaron:
                szurt_konyvek.append({
                    "Könyv Címe": nyers_cim,
                    "Ár (GBP)": ar,
                    "Raktáron": "Igen"
                })

        logging.info(f"Szűrés kész: 20 könyvből {len(szurt_konyvek)} felelt meg a feltételeknek.")

        csv_fajlnev = "olcso_konyvek.csv"
        with open(csv_fajlnev, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["Könyv Címe", "Ár (GBP)", "Raktáron"], delimiter=";")
            writer.writeheader()
            writer.writerows(szurt_konyvek)

        logging.info(f"Szűrt adatok elmentve: {csv_fajlnev}")

    except Exception as e:
        logging.error(f"Kritikus hiba történt a folyamat során: {e}")

if __name__ == "__main__":
    szurt_export_scraper(max_ar=30.0)