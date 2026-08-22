mobilok = [
    "Samsung Galaxy S23",
    "iPhone 15 Pro",
    "Samsung Galaxy A54",
    "Xiaomi Redmi Note 13",
    "Samsung Galaxy S24 Ultra",
    "iPhone 14"
]

Samsungok = []

for telefon in mobilok:
    if "Samsung" in telefon:
        Samsungok.append(telefon)

        print(f"Találtam egy Samsungot: {telefon}")

print(f"A kigyűjtött Samsung telefonok: {Samsungok} ")