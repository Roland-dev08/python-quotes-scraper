import requests
from bs4 import BeautifulSoup
import re
import csv
import time

alap_url = "https://books.toscrape.com/catalogue/"
aktualis_url = "https://books.toscrape.com/catalogue/page-1.html"

minden_konyv = []
fejlec = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

oldal_szamlalo = 1

print("Elindult a dinamikus, teljes oldali bányászat...\n")

while aktualis_url:
    print(f"[{oldal_szamlalo}.oldal] Letöltés: {aktualis_url}")

    valasz = requests.get(aktualis_url, headers=fejlec)
    if valasz.status_code != 200:
        print("Hiba az oldal letöltésekor, leállunk.")
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

    kovetkezo_gomb = leves.select_one("li.next a")

    if kovetkezo_gomb:
        kovetkezo_relativ_link = kovetkezo_gomb["href"]

        aktualis_url = alap_url + kovetkezo_relativ_link
        oldal_szamlalo += 1
        time.sleep(0.5)
    else:
        print("\nElértük az utolsó oldalt, nincs több 'Következő' gomb!")
        aktualis_url = None

with open("osszes_konyv_1000.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["konyv_cime", "ar_gbp"])
    iro.writeheader()
    iro.writerows(minden_konyv)

print(f"\nZseniális! Összesen {len(minden_konyv)} db könyvet bányásztál ki {oldal_szamlalo} oldalról!")