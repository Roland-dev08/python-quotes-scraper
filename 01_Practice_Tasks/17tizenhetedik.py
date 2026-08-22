nyers_ar_1 = "180000 Ft"
nyers_ar_2 = " 12 000 Ft "

print("--- TISZTÍTÁS ELŐTT ---")
print(f"nyers_ar_1 típusa: {type(nyers_ar_1)} (értéke : {nyers_ar_1})")

print("\n--- TISZTÍTÁS FOLYAMATBAN ---")

tiszta_szoveg_1 = nyers_ar_1.replace(" Ft", "")
print("Ft törölve:", tiszta_szoveg_1)

valodi_szam_1 = int(tiszta_szoveg_1)
print(f"Sikeres átalakítás! Új típus: {type(valodi_szam_1)}")

print(f"nyers_ar_2 típusa: {type(nyers_ar_2)} (értéke : {nyers_ar_2})")

print("\n--- TISZTÍTÁS FOLYAMATBAN ---")

tiszta_szoveg_2 = nyers_ar_2.replace(" Ft", "").replace(" ", "")
print("Ft törölve:", tiszta_szoveg_2)

valodi_szam_2 = int(tiszta_szoveg_2)
print(f"Sikeres átalakítás! Új típus: {type(valodi_szam_2)}")

osszeg = valodi_szam_1 + valodi_szam_2

print("\n--- VÉGEREDMÉNY ---")

print(f"a két termék összesen: {osszeg} Ft")