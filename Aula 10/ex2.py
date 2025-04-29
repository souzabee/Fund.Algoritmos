from random import randint, random
m = []
p = []


for num_linha in range (10):
    linha = []
    for num_coluna in range (15):
        linha.append(randint(0, 100))
    m.append(linha)

for linha in range(10):
    for coluna in range(15):
        print(f'{m[linha][coluna]:2d}', end = '')

for linha in range (len(m)):
    print(f'{m[linha][0]}')

        


        
        
