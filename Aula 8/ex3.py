z = []

for n in range (10):
    numero = int(input("Digite um numero: "))
    z.append(numero)
print(z)

maior = float('-inf')
for elemento in z:
    if maior < elemento:
        maior = elemento
print(maior)

for indice in range(len(z)):
    if z[indice] == maior:
        print(f"Maior elemento esta no indice: {indice}")