dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantdidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
tempo_total = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print(f"seu tempo total foi de {tempo_total} segundos")