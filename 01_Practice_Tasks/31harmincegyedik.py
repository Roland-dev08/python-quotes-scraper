import requests
import json

munkamenet = requests.Session()
munkamenet.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

def session_alapu_kaparas():
    print("Munkamenet (Session) indítása...\n")

    suti_url = "https://httpbin.org/cookies/set/bejelentkezve/True"
    print("1. Lépés: Bejelentkezési süti megszerzése...")
    munkamenet.get(suti_url)

    vedett_url = "https://httpbin.org/cookies"
    print("2. Lépés: Védett oldal elérése a munkamenet segítségével...")
    valasz = munkamenet.get(vedett_url)

    if valasz.status_code == 200:
        sutik = valasz.json()
        print("A szerver felismerte az aktív munkamenetet és a sütiket!")

        mentendo_adat = {
            "statusz": "Sikeres munkamenet-megőrzés",
            "detektalt_sutik": sutik.get("cookies", {})
        }

        with open("session_api_adatok.json", "w", encoding="utf-8") as f:
            json.dump(mentendo_adat, f, indent=4, ensure_ascii=False)

        print("Eredmény elmentve a 'session_api_adatok.json' fájlba.")
    else:
        print(f"Hiba a védett oldal elérése során: Status {valasz.status_code}")

if __name__ == "__main__":
    session_alapu_kaparas()