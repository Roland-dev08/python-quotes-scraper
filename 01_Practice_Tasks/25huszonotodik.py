import requests
from bs4 import BeautifulSoup
import csv
import re
import time

alap_url = "https://books.toscrape.com/"
kezdolap_url = "https://books.toscrape.com/index.html"

fejlec = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

valasz = requests.get(kezdolap_url, headers=fejlec)
leves = BeautifulSoup(valasz.text, "html.parser")

kategoria_elemek = leves.select(".side_categories ul.nav-list ul li a")

kategoriak = []
for kat in kategoria_elemek:
    nev = kat.text.strip()
    link = alap_url + kat["href"]
    kategoriak.append({"nev": nev, "url": link})

print(f"Megtalálva: {len(kategoriak)} kategória a weboldalon!\n")

konyv_katalogus = []

for kat in kategoriak[:3]:
    print(f"Kategóri feldolgozása: {kat['nev']}...")

    kat_valasz = requests.get(kat["url"], headers=fejlec)
    kat_leves = BeautifulSoup(kat_valasz.text, "html.parser")

    konyvek = kat_leves.find_all("article")

    for konyv in konyvek:
        cim = konyv.find("h3").find("a")["title"]
        nyers_ar = konyv.find("p", class_="price_color").text
        tiszta_ar = float(re.sub(r'[^\d.]', '', nyers_ar))

        konyv_katalogus.append({
            "konyv_cime": cim,
            "ar_gbp": tiszta_ar,
            "kategoria": kat["nev"]
        })

    time.sleep(0.5)

with open("kategoriak_szerint.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["konyv_cime", "ar_gbp", "kategoria"])
    iro.writeheader()
    iro.writerows(konyv_katalogus)

print(f"\nKész! {len(konyv_katalogus)} könyv kategóriák szerint elmentve a 'kategoriak_szerint.csv' fájlba!")