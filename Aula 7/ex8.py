dia = int(input("Digite o ano: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

def magic (dia, mes, ano):
    if dia * mes == ano % 100:
        return True
    else:
        return False

data_magica = magic (dia, mes, ano)
if data_magica:
    print(f"Data magica: {dia} / {mes} / {ano}")
else:
    print("Não é data magica")
    