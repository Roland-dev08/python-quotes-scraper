rendelések = [12000, 25000, 8000, 15000, 3200]

for összeg in rendelések:
    if összeg >= 15000:
        szállítás = 0
    else:
        szállítás = 1500

    végösszeg = összeg + szállítás
    print(f"Rendelés {összeg} Ft, szállítási díj: {szállítás} Ft, --> Végösszeg: {végösszeg} Ft")