# letra = input("Digite a letra desejada: ")
# if letra == 'a' or letra == 'e' or letra =='i' or letra == 'o' or letra == 'u':
#     print("Essa letra é uma vogal")
# elif letra == 'y':
#     print("Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.")
# else:
#     print("Essa letra é uma consoante.")

# km = int(input("Digite a quantidade de quilometros: "))
# rodados = km/8 * 0.5
# print('Tarifa: ', tarifa)

# planeta = input("Digite o o nome do planeta desejado: ")
# m = float(input("Digite o peso da pessoa na Terra em kg: "))
# def peso (planeta, m):
#     if planeta == 'Vênus':
#         kg = m * 0.88
#         return kg
#     elif planeta == 'Júpiter':
#         kg = m * 2.64
#         return kg
#     elif planeta == 'Mercúrio':
#         kg = m * 0.37
#         return kg
#     elif planeta == 'Marte':
#         kg = m * 0.38
#         return kg
#     elif planeta == 'Saturno':
#         kg = m * 1.15
#         return kg
#     elif planeta == 'Urano':
#         kg = m * 1.17
#         return kg
#     elif planeta == 'Netuno':
#         kg = m * 1.18
#         return kg

# kilo = peso(planeta, m)
# print(f'Peso em {planeta}: {kilo:.2f}')

# l = int(input("Digite a quantidade de linhas: "))
# start = 1
# linha = 0
# for i in range (l):
#     for j in range (3):
#         print(start,end = ' ')
#         start += 1
#     print("PIM")
#     start +=1
        
        


# M = [ ]
# maior = float('-inf')
# ordem = int(input("Digite a ordem da matriz"))
# for num_linha in range (ordem):
#     linha= []
#     for num_coluna in range (ordem):
#         coluna = []
#         n = int(input("Digite um numero: "))
#         linha.append(n)
#     M.append(linha)
# print(f'{M:.3d}')

# ordem = int(input("Digite a ordem da matriz: "))
# n = 1
# z =[]
# for i in range (ordem):
#     linha = []
#     for j in range (ordem):
#         coluna = []
#         linha.append(n)
#     z.append(linha)
        
       
# print(z)


M = []
ordem = int(input("Digite a ordem da matriz: "))  


for num_linha in range(ordem):
    linha = []
    for num_coluna in range(ordem):
    
        n = int(input(f"Digite o elemento da linha {num_linha} e coluna {num_coluna}: "))  
        linha.append(n)  
    M.append(linha)  


result_matrix = []
for row in M:
    result_row = [x * 8 for x in row]  
    result_matrix.append(result_row)


print("Matriz resultante:")
for row in result_matrix:
    print(" ".join(f"{x:2}" for x in row))


















    

