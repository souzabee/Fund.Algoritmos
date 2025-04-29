M = [ ]
for num_linha in range (4):
    linha= []
    for num_coluna in range (4):
        coluna = []
        n = int(input("Digite um numero: "))
        linha.append(n)
    M.append(linha)

for linha in M:
    for elemento in linha:
        print(f'{elemento:2d}', end =' ')
    print()

somas_impares = [0, 0, 0, 0]

for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        if M[linha][coluna] % 2 != 0:
           somas_impares[linha] += M[linha][coluna]
    
print(somas_impares)