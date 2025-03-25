numero = int(input("N: "))
for l in range (numero):
    for c in range(numero):
    
        if l % 2 == 0:
            if c % 2 == 0:
                print("$", end = ' ')
            elif c % 2 != 0:
                print("&", end = ' ')
        if l % 2 != 0:
            if c % 2 == 0:
                    print("%", end = ' ')
            else:
                    print("#", end  = ' ')


    print()
            