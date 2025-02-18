km_totais = float(input("digite a quantidade de km percorridos: "))
dias = int(input("digite a quantidade de dias alocados: "))
valor_total = (60 * dias) + (km_totais * 0.15)
print(f"Total a pagar: {valor_total:.2f}" )