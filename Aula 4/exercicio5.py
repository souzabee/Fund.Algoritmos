id = int(input("Digite o codigo do alimento: "))

if id == 1:
    print("Alimento não perecivel")
elif id >= 2 and id <= 4:
    print("Alimento perecivel")
elif id == 5 or id == 6:
    print("Vestuario")
elif id == 7:
    print("Higiene pessoal")
elif id >= 8 and id <= 15:
    print("Limpeza e utensilios domesticos")
else:
    print("Codigo invalido")