import requests
import json
import time

FEJLEC = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def rejtett_api_kaparasa():
    osszes_idezet = []
    oldal = 1
    van_meg_oldal = True

    print("Rejtett API adatbányászás elindítva...\n")

    while van_meg_oldal:
        api_url = f"https://quotes.toscrape.com/api/quotes?page={oldal}"
        print(f"API kérés küldése: Page {oldal}...")

        valasz = requests.get(api_url, headers=FEJLEC)

        if valasz.status_code == 200:
            adat = valasz.json()
            idezetek = adat.get("quotes", [])
            for item in idezetek:
                osszes_idezet.append({
                    "szerzo": item["author"]["name"],
                    "idezet": item["text"],
                    "cimkek": item["tags"]
                })

            van_meg_oldal = adat.get("has_next", False)
            oldal += 1
            time.sleep(0.5)
        else:
            print(f"Hiba az API kérés során: Status{valasz.status_code}")
            break

    with open("rejtett_api_idezetek.json", "w", encoding="utf-8") as f:
        json.dump(osszes_idezet, f, indent=4, ensure_ascii=False)

    print(f"\nSiker! {len(osszes_idezet)} db. idézet elmentve a 'rejtett_api_idezetek.json' fájlba.")

if __name__ == "__main__":
    rejtett_api_kaparasa()