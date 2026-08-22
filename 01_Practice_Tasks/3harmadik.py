pontszámok = [85, 42, 98, 60, 15, 74]

saját_pont = int(input("Kérem a pontszámot: "))

pontszámok.append(saját_pont)

for pont in pontszámok:
    if pont >=80:
        # 1. SZABADKÉZ: Ide jön a kódod, ha a pont 80 vagy több.
        print(f"A {pont} pontos eredmény: KITŰNŐ!😏")

    elif pont >= 50:
        # 2. SZABADKÉZ: Ide jön a kódod, ha a pont 50 és 79 között van.
        print(f"A {pont} pontos eredmény: SIKERES vizsga!👌")

   
    else:
        # 3. SZABADKÉZ: Minden más esetben (50 alatt).
        print(f"A {pont} pontos eredmény: A vizsga SAJNOS NEM SIKERÜLT.😞")