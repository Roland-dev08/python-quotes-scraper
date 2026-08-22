import csv
from bs4 import BeautifulSoup
import re

html_kod = """
<div class="termek-kartya">
    <span class="termek-nev">Lenovo Laptop</span>
    <span class="termek-ar">180000 Ft</span>
</div>
<div class="termek-kartya">
    <span class="termek-nev">Logitech Egér</span>
    <span class="termek-ar">12 000 Ft</span>
</div>
<div class="termek-kartya">
    <span class="termek-nev">HP Monitor</span>
    <span class="termek-ar">65000 Ft</span>
</div>
"""
leves = BeautifulSoup(html_kod, "html.parser")
termek_kartyak = leves.find_all("div", class_="termek-kartya")

webshop_adatok = []

print("--- ADATBÁNYÁSZAT ÉS TISZTÍTÁS INDÍTÁSA ---")

for kartya in termek_kartyak:
    nev = kartya.find(class_="termek-nev").text
    nyers_ar = kartya.find(class_="termek-ar").text

    tiszta_szoveg = re.sub(r'\D', '', nyers_ar)
    tiszta_ar = int(tiszta_szoveg) if tiszta_szoveg else 0

    termek_szotar = {
        "termek_neve": nev,
        "termek_ara": tiszta_ar
    }

    webshop_adatok.append(termek_szotar)
    print(f"Sikeresen tisztítvaÉ {nev} -> {tiszta_ar} (Típus: {type(tiszta_ar)})")

with open("tiszta_termekek.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["termek_neve", "termek_ara"])
    iro.writeheader()
    iro.writerows(webshop_adatok)

print("\nKész! Az adatok letisztítva elmentve a 'tiszta_termekek.csv' fájlba!")