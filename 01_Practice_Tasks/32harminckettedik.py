import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import json

def robusztus_api_keres():
    print("Robusztus, hibakereső API kliens indítása...\n")

    retry_strategia = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )

    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry_strategia)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

    target_url = "https://quotes.toscrape.com/api/quotes?page=1"

    try:
        print("Kérés küldése (automatikus újrapróbálkozás aktív)...")
        valasz = session.get(target_url, timeout=5)

        if valasz.status_code == 200:
            adat = valasz.json()
            with open("hibaturo_api_adat.json", "w", encoding="utf-8") as f:
                json.dump(adat.get("quotes", [])[:3], f, indent=4, ensure_ascii=False)
            print("\nMűködő teszadatok elmentve a 'hibaturo_api_adat.json' fájlba.")
        else:
            print(f"Státuszkód: {valasz.status_code}")

    except Exception as e:
        print(f"Végleges hiba: {e}")

if __name__ == "__main__":
    robusztus_api_keres()