π = 3.1415
from math import ceil
raio = float(input("Raio do cilindro: "))
altura = float(input("Altura cilindro: "))


litros = π * altura * raio ** 2
area_lateral = 2 * π * raio * altura
area_base =  2 * π * raio ** 2
area_total = area_lateral + area_base
latas_necessarias = area_total / 15
latas = 50

print(f"Area a ser pintada: {area_total:.2f}")
print(f"Quantidade de litros necessarios: {litros:.2f}")
print(f"A area da base é: {area_base:.2f}")

if latas_necessarias <= 1:
    print(f"Quantidade de latas de tinta: {latas_necessarias:.0f}")
    print((f"Custo total: {latas:.0f}"))

if 1 < latas_necessarias <= 2:
    latas2 = latas - 2
    custo_total1 = latas2 * 2
    print(f"Quantidade de latas de tinta: {latas_necessarias:.0f}")
    print(f"Custo total: {custo_total1:.0f}")
    

if 2 < latas_necessarias <= 3:
    latas3 = latas - 4
    custo_total2 = latas3 * 2
    print(f"Quantidade de latas de tinta: {latas_necessarias:.0f}")
    print(f"Custo total: {custo_total2:.0f}")

if latas_necessarias > 3:
    latas4 = latas - 5
    custo_total3 = latas4 * 2
    print(f"Quantidade de latas de tinta: {latas_necessarias:.0f}")
    print(f"Custo total: {custo_total3:.0f}")
