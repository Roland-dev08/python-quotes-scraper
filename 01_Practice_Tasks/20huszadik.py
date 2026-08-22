import requests
from bs4 import BeautifulSoup
import re
import csv

url = "https://books.toscrape.com/index.html"

fejlec = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

valasz = requests.get(url, headers=fejlec)
leves = BeautifulSoup(valasz.text, "html.parser")

konyvek = leves.find_all("article")

konyv_lista = []

for konyv in konyvek:
    cim = konyv.find("h3").find("a")["title"]
    nyers_ar = konyv.find("p", class_="price_color").text
    tiszta_ar = float(re.sub(r'[^\d.]', '', nyers_ar))

    konyv_lista.append({
        "konyv_cime": cim,
        "ar_gbp": tiszta_ar
    })

with open("konyvek.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["konyv_cime", "ar_gbp"])
    iro.writeheader()
    iro.writerows(konyv_lista)

print(f"Siker! {len(konyv_lista)} db könyv adatai elmentve a 'konyvek.csv' fájlba!")