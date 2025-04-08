z = []

for n in range (10):
    num = int(input("Digite um numero: "))
    z.append(num)

for indice in range (2, len(z)):
    if z[indice] > z[indice - 1] + z[indice - 2]:
        print(z[indice])

       