import csv

with open("olcso_termekek.csv", "r", encoding="utf-8") as fajl:
    olvaso = csv.DictReader(fajl)

    print("--- ADATOK BEOLVASÁSA A FÁJLBÓL ---")

    for sor in olvaso:
        nev = sor["nev"]
        ar = sor["ar"]

        print(f"Termék: {nev}, Ár: {ar} Ft")