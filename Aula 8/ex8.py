z = []

while True:
    pala = input("Digite uma palavra: ")
    if pala == "":
        break
    else:
        if pala not in z:
            z.append(pala)
    
for itens in z :
    print(itens)