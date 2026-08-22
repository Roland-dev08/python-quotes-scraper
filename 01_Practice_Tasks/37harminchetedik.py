import requests
from bs4 import BeautifulSoup
import json
import re

def ar_tisztitas(nyers_ar):
    talalat = re.search(r"[\d.]+", nyers_ar)
    if talalat:
        return float(talalat.group())
    return 0.0

def keszlet_konvertalas(nyers_keszlet):
    return "In stock" in nyers_keszlet

def adat_tisztito_scraper():
    print("Adatgyűjtés és professzionális adattisztítás...\n")
    url = "https://books.toscrape.com/"

    valasz = requests.get(url)
    soup = BeautifulSoup(valasz.text, "html.parser")

    tisztitott_konyvek = []

    for termek in soup.select("article.product_pod"):
        nyers_cim = termek.h3.a["title"]
        nyers_ar = termek.select_one("p.price_color").text
        nyers_keszlet = termek.select_one("p.instock.availability").text.strip()

        tisztitott_konyvek.append({
            "cim": nyers_cim,
            "ar_gbp": ar_tisztitas(nyers_ar),
            "van_raktaron": keszlet_konvertalas(nyers_keszlet)
        })

    with open("tisztitott_konyvek.json", "w", encoding="utf-8") as f:
        json.dump(tisztitott_konyvek, f, indent=4, ensure_ascii=False)

    print("Tiszta, strukturált adatok elmentve a 'tisztitott_konyvek.json' fájlba!")

if __name__ == "__main__":
    adat_tisztito_scraper()