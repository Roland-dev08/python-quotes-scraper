import requests
from bs4 import BeautifulSoup
import csv
import re

def ar_tisztitas(nyers_ar):
    talalat = re.search(r"[\d.]+", nyers_ar)
    return float(talalat.group()) if talalat else 0.0

def csv_export_scraper():
    print("Adatgyűjtés és exportálás Excel-barát CSV fájlba...\n")
    url = "https://books.toscrape.com/"

    valasz = requests.get(url)
    soup = BeautifulSoup(valasz.text, "html.parser")

    tisztitott_konyvek = []

    for termek in soup.select("article.product_pod"):
        nyers_cim = termek.h3.a["title"]
        nyers_ar = termek.select_one("p.price_color").text
        nyers_keszlet = termek.select_one("p.instock.availability").text.strip()

        tisztitott_konyvek.append({
            "Könyv Címe": nyers_cim,
            "Ár (GBP)": ar_tisztitas(nyers_ar),
            "Raktáron": "Igen" if "In stock" in nyers_keszlet else "Nem"
        })

    csv_fajlnev = "konyvek_export.csv"
    mezonevek = ["Könyv Címe", "Ár (GBP)", "Raktáron"]

    with open(csv_fajlnev, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=mezonevek, delimiter=";")

        writer.writeheader()

        writer.writerows(tisztitott_konyvek)

    print(f"Sikeres export! A(z) '{csv_fajlnev}' fájl készen áll, megnyitható Excelben.")

if __name__ == "__main__":
    csv_export_scraper()



