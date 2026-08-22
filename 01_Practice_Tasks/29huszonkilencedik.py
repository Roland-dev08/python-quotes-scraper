import requests
import json
import time

BASE_API_URL = "https://quotes.toscrape.com/api/quotes"
FEJLEC = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def api_lekeresese_parameterekkel():
    osszes_idezet = []
    oldal = 1
    van_meg = True

    print("API adatbányászás paraméterekkel elindítva...\n")

    while van_meg:
        query_params = {
            "page": oldal,
        }

        valasz = requests.get(BASE_API_URL, headers=FEJLEC, params=query_params)

        if valasz.status_code == 200:
            adat = valasz.json()
            idezetek = adat.get("quotes", [])

            for item in idezetek:
                osszes_idezet.append({
                    "szerzo": item["author"]["name"],
                    "idezet": item["text"],
                    "cimkek_szama": len(item["tags"]),
                    "elso_cimke": item["tags"][0] if item["tags"] else "Nincs"
                })

            print(f"Oldal {oldal} feldolgozva, {len(idezetek)} db. idézet kinyerve.")

            van_meg = adat.get("has_next", False)
            oldal += 1
            time.sleep(0.3)
        else:
            print(f"Hiba az API kérés során: Status {valasz.status_code}")
            break

    albert_einstein_idezetek = [i for i in osszes_idezet if i["szerzo"] == "Albert Einstein"]

    mentendo_adat = {
        "osszesen_kinyerve": len(osszes_idezet),
        "einstein_idezetek_szama": len(albert_einstein_idezetek),
        "idezetek": osszes_idezet
    }

    with open("professzionalis_api_adatok.json", "w", encoding="utf-8") as f:
        json.dump(mentendo_adat, f, indent=4, ensure_ascii=False)

    print(f"\nSiker! {len(osszes_idezet)} db. idézet elmentve (ebből {len(albert_einstein_idezetek)} db. Albert Einstein idézet) a 'professzionalis_api_adatok.json' fájlba.")

if __name__ == "__main__":
    api_lekeresese_parameterekkel()