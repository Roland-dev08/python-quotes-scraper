osszes_ar = [4500, 12000, 2500, 18500, 9000, 32000, 1500]

premium_termekek = []

for ar in osszes_ar:
    if ar >= 15000:
        premium_termekek.append(ar)

        print(f"Megvan! Mentve a prémium listába: {ar} Ft")

print(f"A prémium termékek listája: {premium_termekek}")