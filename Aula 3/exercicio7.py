d = float(input("Distancia desejada (em km): "))

if d > 200:
   d1 = d * 0.5
   print(f"{d1:.2f}")

else:
    d2 = d * 0.45
    print(f"{d2:.2f}")