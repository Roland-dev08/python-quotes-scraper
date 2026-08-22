import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import json
import random
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"
]

def generalj_alcazott_fejlecet():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7",
        "Sec-Ch-Ua": '"Not A (Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate"
    }

def emberi_szunet(min_s=1.2, max_s=2.8):
    varakozas = random.uniform(min_s, max_s)
    time.sleep(varakozas)

def hozz_letre_robusztus_sessiont():
    session = requests.Session()
    retry_strategia = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry_strategia)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def könyv_adatok_kinyerese(html_tartalom):
    soup = BeautifulSoup(html_tartalom, "html.parser")
    konyvek = []

    for termek in soup.select("article.product_pod"):
        cím = termek.h3.a["title"]
        ár = termek.select_one("p.price_color").text
        készlet = termek.select_one("p.instock.availability").text.strip()

        konyvek.append({
            "cim": cím,
            "ar": ár,
            "keszleten": készlet
        })
    return konyvek

def mester_scraper():
    print("Moduláris Mester-Scraper inítása...\n")
    session = hozz_letre_robusztus_sessiont()
    osszes_konyv = []

    alap_url = "https://books.toscrape.com/catalogue/page-{}.html"

    for oldal in range(1, 3):
        url = alap_url.format(oldal)
        fejlec = generalj_alcazott_fejlecet()

        print(f"Oldal #{oldal} lekérése...")
        try:
            valasz = session.get(url, headers=fejlec, timeout=10)
            if valasz.status_code == 200:
                oldal_konyvei = könyv_adatok_kinyerese(valasz.text)
                osszes_konyv.extend(oldal_konyvei)
                print(f"{len(oldal_konyvei)} könyv sikeresen feldolgozva.")
            else:
                print("Sátuszkód: {valasz.status_code}")
        except Exception as e:
            print(f"Hálózati hiba az oldalon: {e}")

        emberi_szunet()

    with open("mester_konyv_adatok.json", "w", encoding="utf-8") as f:
        json.dump(osszes_konyv, f, indent=4, ensure_ascii=False)

    print(f"\nÖsszesen {len(osszes_konyv)} könyv adatmentése elvégezve a 'mester_konyv_adatok.json' fájlba!")

if __name__ == "__main__":
    mester_scraper()