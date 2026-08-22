import csv

termekek = [
    {"nev": "Samsung Galaxy S23", "ar": 280000},
    {"nev": "Xiaomi fülhalgató", "ar": 15000},
    {"nev": "iPhone tok", "ar": 8000},
    {"nev": "Samsung monitor", "ar": 95000},
    {"nev": "Asus Laptop", "ar": 320000},
    {"nev": "Okosóra", "ar": 45000}
]

olcso_termekek = []

for termek in termekek:

    nev = termek["nev"]
    ar = termek["ar"]

    if ar < 50000:
        olcso_termekek.append(termek)

with open("olcso_termekek.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["nev", "ar"])
    iro.writeheader()
    iro.writerows(olcso_termekek)

print(f"A fájl elmentve! Nézz rá a bal oldali sávra (Explorer)!")