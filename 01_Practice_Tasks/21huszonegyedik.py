import requests
from bs4 import BeautifulSoup
import re
import csv
import time

minden_konyv = []

fejlec = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

for oldal in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{oldal}.html"
    print(f"Letöltés folyamatban: {oldal}. oldal...")

    valasz = requests.get(url, headers=fejlec)

    if valasz.status_code != 200:
       print(f"A(z) {oldal}. oldal nem érhető el!")
       break

    leves = BeautifulSoup(valasz.text, "html.parser")
    konyvek = leves.find_all("article")

    for konyv in konyvek:
        cim = konyv.find("h3").find("a")["title"]
        nyers_ar = konyv.find("p", class_="price_color").text
        tiszta_ar = float(re.sub(r'[^\d.]', '', nyers_ar))

        minden_konyv.append({
            "konyv_cime": cim,
            "ar_gbp": tiszta_ar
        })

    time.sleep(1)

with open("minden_konyv.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["konyv_cime", "ar_gbp"])
    iro.writeheader()
    iro.writerows(minden_konyv)

print(f"\nKész! Összesen {len(minden_konyv)} db könyv adatai elmentve a 'minden_konyv.csv' fájlba!")