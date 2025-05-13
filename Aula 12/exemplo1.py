#Modelo: 
# arquivo = open("teste.txt", 'w')

# for linha in range (1, 101):
#     arquivo.write("Linha %d\n" % linha)
# arquivo.close()

# arquivo = open('teste.txt', 'r')

# for linha in arquivo.readline():
#     print(linha.strip())
# arquivo.close()

pares = open('pares.txt', 'w')
impares = open('impares.txt', 'w')

for linha in range (1, 999):
    if linha % 2 == 0:
        pares.write("Numero: %d\n" % linha)
    if linha % 2 != 0:
        impares.write("Numero: %d\n" % linha)
    