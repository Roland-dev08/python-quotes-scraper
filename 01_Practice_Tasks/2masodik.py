# 1. Letrehozunk egy listat a termekarakkal
arak = [19, 45, 9, 99, 15, 120, 8]

# 2. A ciklussal vegigmegyunk az arakon egyenkent
for ar in arak:
    # 3. Megvizsgaljuk,hogy az  aktualis ar kisebb-e, mint 20
    if ar < 20:
        print(f"Talaltam egy olcso termeket! Csak {ar} euro.")