import requests
import json
import random
import time

def emberi_szunet():
    varakozas = random.uniform(1.0, 2.5)
    time.sleep(varakozas)

def get_profi_fejlec():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Ch-Ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1"
    }

def profi_alcazas_teszt():
    print("Teljes böngésző-ujjlenyomat szimulálása...\n")

    session = requests.Session()
    session.headers.update(get_profi_fejlec())

    STABIL_URL = "https://postman-echo.com/get"

    try:
        valasz = session.get(STABIL_URL, timeout=10)
        if valasz.status_code == 200:
            adatok = valasz.json()
            print("A szerver sikeresen feldolgozta a kérést!")

            with open("profi_fejlec_kimenet.json", "w", encoding="utf-8") as f:
                json.dump(adatok.get("headers", {}), f, indent=4, ensure_ascii=False)
            print("A szerver által észlelt teljes fejléc elmentve a 'profi_fejlec_kimenet.json' fájlba.")
    except Exception as e:
        print(f"Hiba: {e}")

if __name__ == "__main__":
    emberi_szunet()
    profi_alcazas_teszt()