árak_eur = [5, 12, 50, 120, 3]

for ár in árak_eur:

    ár_huf = ár * 400

    if ár_huf > 10000:
        print(f"A termék ára {ár_huf} Ft, ami drága.")
    else:
        print(f"A termék ára {ár_huf} Ft, ami megfizethető.")