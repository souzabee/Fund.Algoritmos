ano_fabric = int(input("Ano de fabricação do carro: "))
ano_atual = int(input("Ano atual: "))

c_idade = ano_atual - ano_fabric


if c_idade < 3:
    print("Carro novo")

else:
    print("Carro velho")