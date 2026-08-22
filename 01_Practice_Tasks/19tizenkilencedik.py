import requests
from bs4 import BeautifulSoup
import re

url = "https://books.toscrape.com/index.html"

fejlec = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

valasz = requests.get(url, headers=fejlec)

print(f"Szerver válaszkódja: {valasz.status_code}")

leves = BeautifulSoup(valasz.text, "html.parser")

if leves.title:
    print(f"Oldal címe: {leves.title.text.strip()}")

konyvek = leves.find_all("article")

print(f"Sikeresen megtalálva: {len(konyvek)} db könyv a kezdőlapon!\n")

for konyv in konyvek:
    cim = konyv.find("h3").find("a")["title"]
    nyers_ar = konyv.find("p", class_="price_color").text

    tiszta_ar = float(re.sub(r'[^\d.]', '', nyers_ar))

    print(f"📖 Könyv: {cim:<50} | 💰Ár: {tiszta_ar} $")