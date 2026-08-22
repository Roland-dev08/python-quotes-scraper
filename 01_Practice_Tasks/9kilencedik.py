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

        print(f"Olcsó termék megtalálva: {nev} ({ar} Ft)")

print(f"Az olcsó termékek listája: {olcso_termekek}")
