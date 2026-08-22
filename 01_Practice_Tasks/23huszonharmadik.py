import requests
from bs4 import BeautifulSoup
import re
import csv
import time

alap_url = "https://books.toscrape.com/catalogue/"
kezdolap_url = "https://books.toscrape.com/catalogue/page-1.html"

fejlec = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

valasz = requests.get(kezdolap_url, headers=fejlec)
leves = BeautifulSoup(valasz.text, "html.parser")

konyv_kartyak = leves.find_all("article")[:5]

reszletes_adatok = []

print("Mélyfúrás indítása az egyes könyvek aloldalaira...\n")

for kartya in konyv_kartyak:
    relativ_link = kartya.find("h3").find("a")["href"]
    reszletes_url = alap_url + relativ_link
    try:
        aloldal_valasz = requests.get(reszletes_url, headers=fejlec)
        aloldal_leves = BeautifulSoup(aloldal_valasz.text, "html.parser")

        cim = aloldal_leves.find("h1").text

        nyers_ar = aloldal_leves.find("p", class_="price_color").text
        tiszta_ar = float(re.sub(r'[^\d.]', '', nyers_ar))

        nyers_raktar = aloldal_leves.find("p", class_="instock availability").text

        raktar_db = int(re.sub(r'\D', '', nyers_raktar))

        reszletes_adatok.append({
            "konyv_cime": cim,
            "ar_gbp": tiszta_ar,
            "raktarkeszlet_db": raktar_db
        })

        print(f"Siker: {cim[:30]}... | Ár: {tiszta_ar} $ | Raktáron: {raktar_db} db")
        time.sleep(0.5)

    except Exception as hiba:
        print(f"HIBA történt ennél a könyvnél ({reszletes_url}): {hiba}")

with open("reszletes_konyvek.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["konyv_cime", "ar_gbp", "raktarkeszlet_db"])
    iro.writeheader()
    iro.writerows(reszletes_adatok)

print(f"\nKész! {len(reszletes_adatok)} könyv mélyfúrása elmentve a 'reszletes_könyvek.csv' fájlba!")