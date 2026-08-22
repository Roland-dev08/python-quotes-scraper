import csv

konyvek = []

with open("osszes_konyv_1000.csv", "r", encoding="utf-8") as fajl:
    olvaso = csv.DictReader(fajl)
    for sor in olvaso:
        konyvek.append({
            "cím": sor["konyv_cime"],
            "ár": float(sor["ar_gbp"])
        })

print(f"Sikeresen beolvasva: {len(konyvek)} db könyv az adatbázisból.\n")

osszesen_ar = sum(konyv["ár"] for konyv in konyvek)
atlag_ar = osszesen_ar / len(konyvek)

legolcsobb = min(konyvek, key=lambda k: k["ár"])
legdragabb = max(konyvek, key=lambda k: k["ár"])

olcso_konyvek = [k for k in konyvek if k["ár"] < 20.0]

print("=== KÖNYVÁRUHÁZ STATISZTIKA ===")
print(f"Átlag könyvár: {atlag_ar:.2f} $")
print(f"Legolcsóbb könyv: {legolcsobb['cím']} ({legolcsobb['ár']} $)")
print(f"Legdrágább könyv: {legdragabb['cím']} ({legdragabb['ár']} $)")
print(f"20 $ alatti akcióban elérhető: {len(olcso_konyvek)} db könyv")

with open("akcios_konyvek_20_alatti.csv", "w", encoding="utf-8", newline="") as fajl:
    iro = csv.DictWriter(fajl, fieldnames=["konyv_cime", "ar_gbp"])
    iro.writeheader()
    for konyv in olcso_konyvek:
        iro.writerow({"konyv_cime": konyv["cím"], "ar_gbp": konyv["ár"]})

print("\nAz akciós könyvek külön elmentve az 'akcios_konyvek_20_alatt.csv' fájlba!")