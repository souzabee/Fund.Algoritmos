ano_atual = int(input("Digite o ano atual: "))
data_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - data_nascimento

if idade > 18:
    print("Você pode tirar a CNH!!")

if idade < 18:
    print("Você não pode tirar a CNH")