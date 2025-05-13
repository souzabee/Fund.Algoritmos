multiplos = open('multiplos.txt', 'w')
pares = open('pares.txt', 'r')

for linha in pares.readlines():
    numero = int(linha)
    if numero % 2 == 0:
        multiplos.write("Numero: %d\n" % numero)
    

