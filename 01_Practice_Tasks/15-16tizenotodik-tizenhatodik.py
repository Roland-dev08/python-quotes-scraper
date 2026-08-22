import csv

from bs4 import BeautifulSoup

html_kod = """
<div class="bolt">
    <div class="termek-kartya">
        <h2 class="termek-nev">Lenovo Laptop</h2>
        <span class="termek-ar">180000 Ft</span>
    </div>
    <div class="termek-kartya">
        <h2 class="termek-nev">Logitech Egér</h2>
        <span class="termek-ar">12000 Ft</span>
    </div>
    <div class="termek-kartya">
        <h2 class="termek-nev">HP Monitor</h2>
        <span class="termek-ar">65000 Ft</span>
    </div>
</div>
"""

leves = BeautifulSoup(html_kod, "html.parser")

termek_kartyak = leves.find_all("div", class_="termek-kartya")

webshop_adatok = []

print("--- ADATBÁNYÁSZAT INDÍTÁSA ---")

for kartya in termek_kartyak:
    nev = kartya.find(class_="termek-nev").text
    ar = kartya.find(class_="termek-ar").text

    termek_szotar = {
        "termek_neve": nev,
        "termek_ara": ar
    }

    webshop_adatok.append(termek_szotar)
    
    print(f"Sikeresen kiolvasva: {nev} -> {ar}")

print("\nA bányászat végeredménye (az összesített lista):")

print(webshop_adatok)

with open("webshop_termekek.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["termek_neve", "termek_ara"])

    iro.writeheader()
    iro.writerows(webshop_adatok)

print("Bányászat kész, adatok elmentve a 'webshop_termekek.csv' fájlba!")