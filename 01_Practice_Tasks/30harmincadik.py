import requests
import json

API_URL = "https://httpbin.org/post"

FEJLEC = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}

def post_api_kaparas():
    print("POST kérés és adatcsomag (Payload) küldése...\n")

    keresesi_szurok = {
        "kategoria": "könyvek",
        "minimum_ar": 15.0,
        "maximum_ar": 50.0,
        "rendezes": "ar_szerint_novekvo",
        "raktaron_van": True
    }

    valasz = requests.post(API_URL, headers=FEJLEC, json=keresesi_szurok)

    if valasz.status_code == 200:
        eredmeny = valasz.json()
        print("A szerver feldolgozta a POST kérést és visszajelezte a kapott adatokat!")

        felfogott_payload = eredmeny.get("json", {})

        mentendo_adat = {
            "statusz": "Sikeres POST kommunikáció",
            "kuldott_szurok": felfogott_payload,
            "kliens_ip": eredmeny.get("origin")
        }

        with open("post_api_adatok.json", "w", encoding="utf-8") as f:
            json.dump(mentendo_adat, f, indent=4, ensure_ascii=False)

        print("Eredmény elmentve a 'post_api_adatok.json' fájlba.")
    else:
        print(f"Hiba a POST kérés során: Status {valasz.status_code}")

if __name__ == "__main__":
    post_api_kaparas()