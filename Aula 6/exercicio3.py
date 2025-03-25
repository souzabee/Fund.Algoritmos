numero = int(input("N numeros: "))


for l in range (numero):
    for j in range (numero):
        if (1 + j) % 2 == 0:
            print("o", end = ' ')
        else:
            print("x", end = ' ')
    print()
        