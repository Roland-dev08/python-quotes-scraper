import requests
import random
import time

def emberi_szunet(min_mp=1.5, max_mp=3.5):
    varakozas = random.uniform(min_mp, max_mp)
    print(f"Emberi viselkedés szimulálása: várakozás {varakozas:.2f} másodpercig...")
    time.sleep(varakozas)

def szimulalt_banyaszat():
    print("Inteligens, változó ritmusú adatgyűjtés elindítva...\n")

    urls = [
        "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
        "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
    ]

    for index, url in enumerate(urls, 1):
        print(f"Oldal #{index} lekérése...")
        valasz = requests.get(url)
        print(f"Sikeres letöltés! Státusz: {valasz.status_code}")

        emberi_szunet(1.5, 3.5)

    print("\nFolyamat befelyezve! A kérések ritmusa teljesen természetes volt.")

if __name__ == "__main__":
    szimulalt_banyaszat()