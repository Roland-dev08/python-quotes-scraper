import requests
from bs4 import BeautifulSoup
import re
import json
import time

FEJLEC ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def oldal_letoltese(url):
    try:
        valasz = requests.get(url, headers=FEJLEC, timeout=10)
        if valasz.status_code == 200:
            return BeautifulSoup(valasz.text, "html.parser")
    except Exception as e:
        print(f"Hiba a letöltés során ({url}): {e}")
    return None

def konyvek_kibanyaszasa(leves):
    konyv_lista = []
    kartyat = leves.find_all("article")

    for konyv in kartyat:
        cim = konyv.find("h3").find("a")["title"]
        nyers_ar = konyv.find("p", class_="price_color").text
        tiszta_ar = float(re.sub(r"[^\d.]", "", nyers_ar))

        konyv_lista.append({
            "cim": cim,
            "ar_gbp": tiszta_ar
        })
    return konyv_lista

def mentes_jsonbe(adatok, fajlnev="modularis_adatok.json"):
    with open(fajlnev, "w", encoding="utf-8") as f:
        json.dump(adatok, f, ensure_ascii=False, indent=4)
    print(f"\nAdatok sikeresen elmentve a '{fajlnev}' fájlba.")

def main():
    print("Moduláris adatbányászás elindítva...\n")
    kezdolap_url = "https://books.toscrape.com/index.html"
    leves = oldal_letoltese(kezdolap_url)

    if not leves:
        print("Nem sikerült elindítani a kaparást.")
        return

    konyvek = konyvek_kibanyaszasa(leves)
    print(f"Sikeresen kinyerve {len(konyvek)} db. könyv.")

    mentes_jsonbe(konyvek)

if __name__ == "__main__":
    main()