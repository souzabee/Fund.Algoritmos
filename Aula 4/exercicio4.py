nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2025

idade = ano_atual - nascimento

if idade >= 16:
    print("Pode votar")
    if idade >= 18:
        print("Pode dirigir")

