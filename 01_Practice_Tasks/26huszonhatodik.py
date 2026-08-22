import requests
from bs4 import BeautifulSoup
import re
import json
import time

alap_url = "https://books.toscrape.com/"
kezdolap_url = "https://books.toscrape.com/index.html"

fejlec = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

valasz = requests.get(kezdolap_url, headers=fejlec)
leves = BeautifulSoup(valasz.content, "html.parser")

kategoria_elemek = leves.select(".side_categories ul.nav-list ul li a")

kategoria_adatbazis = {}

for kat in kategoria_elemek[:3]:
    kat_nev = kat.text.strip()
    kat_url = alap_url + kat["href"]

    print(f"Kategória feldolgozása JSON-hez: {kat_nev}...")

    kat_valasz = requests.get(kat_url, headers=fejlec)
    kat_leves = BeautifulSoup(kat_valasz.content, "html.parser")
    konyvek = kat_leves.find_all("article")

    konyv_lista = []
    for konyv in konyvek:
        cim = konyv.find("h3").find("a")["title"]
        nyers_ar = konyv.find("p", class_="price_color").text
        tiszta_ar = float(re.sub(r"[^\d.]", "", nyers_ar))

        konyv_lista.append({
            "cim": cim,
            "ar_gbp": tiszta_ar
        })

    kategoria_adatbazis[kat_nev] = konyv_lista
    time.sleep(0.5)

with open("kategoriak.json", "w", encoding="utf-8") as fajl:
    json.dump(kategoria_adatbazis, fajl, ensure_ascii=False, indent=4)

print("\nSiker! Az adatok hierarchikusan elmentve a 'kategoriak.json' fájlba.")
        
        