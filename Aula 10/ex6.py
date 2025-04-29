from random import randint, random
m = []
for num_linha in range (12):
    linha = []
    for num_coluna in range (12):
        linha.append(randint(0, 10))
    m.append(linha)

for linha in range(12):
    for coluna in range(12):
        print(f'{m[linha][coluna]:2d}', end = ' ')
    print()

contador_media = 0
soma = 0
for n_linhas in range(len(m)):
    for n_colunas in range(len(m)):
        if n_linhas > n_colunas:
            contador_media = contador_media + 1
            soma += m[n_linhas][n_colunas]

            

n = input("")

if n == "S":
    print(soma)
elif n == "M":
    if contador_media > 0:
        media = soma / contador_media
    else:
        media = 0
    print(media)