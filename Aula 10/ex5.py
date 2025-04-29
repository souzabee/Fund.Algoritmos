from random import randint, random
m = []
for num_linha in range (10):
    linha = []
    for num_coluna in range (5):
        linha.append(randint(0, 10))
    m.append(linha)

for linha in range(10):
    for coluna in range(5):
        print(f'{m[linha][coluna]:2d}', end = ' ')
    print()

mt = []

for n_linha in range (5):
    linha = []
    for n_coluna in range (10):
        linha.append(m[n_coluna][n_linha])
    mt.append(linha)

print()


for linha in mt:
    for elemento in linha:
        print(f'{elemento:2d}', end=' ')
    print()



