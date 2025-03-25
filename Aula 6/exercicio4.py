numero = int(input("N: "))
for l in range (numero):
    for c in range (numero):
        if c < l:
            print("$", end = ' ')
        elif c >= l:
            print("@", end = ' ')
            
    
        
    print()