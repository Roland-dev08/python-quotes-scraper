import requests
import json
import random
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Applewebkit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Mozzila/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
]

def dinamikus_fejlec_generalas():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "hu-HU,hu;q=0.9,en-US;q=0.8"
    }
        
def user_agent_rotacio_teszt():
    print("User-Agent rotációs teszt inítása...\n")
    naplo = []

    STABIL_URL = "https://postman-echo.com/get"

    for i in range(1, 4):
        fejlec = dinamikus_fejlec_generalas()
        print(f"Kérés #{i} küldése ezzel az álcával:\n  --> {fejlec['User-Agent'][:65]}...")

        try:
            valasz = requests.get(STABIL_URL, headers=fejlec, timeout=5)
            if valasz.status_code == 200:
                detektalt = valasz.json()
                szerver_ua = detektalt.get("headers", {}).get("user-agent")

                naplo.append({
                    "keres_szama": i,
                    "szerver_altal_latott_ua": szerver_ua
                })
                print(f"Visszaigazolt álca: {szerver_ua[40]}...")
            else:
                print(f"Váratlan státuszkód: {valasz.status_code}")
        except Exception as e:
            print(f"Hálózati hiba: {e}")

        time.sleep(1)

    with open("user_agent_rotation.json", "w", encoding="utf-8") as f:
        json.dump(naplo, f, indent=4, ensure_ascii=False)

    print("\nSiker! A User-Agent rotáció elmentve a 'user_agent_rotacio.json' fájlba!")

if __name__ == "__main__":
    user_agent_rotacio_teszt()