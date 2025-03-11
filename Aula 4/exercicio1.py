id = int(input("Digite o código do produto: "))

if id == 1:
    print("Produto do Sul")
elif id == 2:
    print("Produto do Norte")
elif id == 3:
    print("Produto do Leste")
elif id == 4:
    print("Produto do Oeste")
elif id == 5 or id == 6:
    print("Produto do Nordeste")
elif id >= 7 and id <= 9:
    print("Produto do Sudeste")
elif id >= 10 and id <= 20:
    print("Produto do Centro-oeste")
elif id >= 25 and id <= 30:
    print("Produto do Nordeste")
else:
    print("Produto importado")