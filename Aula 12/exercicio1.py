invertidos = open('invertidos.txt', 'w')
pares = open('pares.txt', 'r')
z = []
for numeros in pares.readlines():
    z.append(numeros)
z.reverse()

for linha in z:
    invertidos.write(linha)




