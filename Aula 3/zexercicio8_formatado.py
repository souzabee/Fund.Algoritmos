π = 3.1415
from math import ceil
raio = float(input("Raio do cilindro: "))
altura = float(input("Altura cilindro: "))


litros = π * altura * raio ** 2
area_lateral = 2 * π * raio * altura
area_base =  π * raio ** 2
area_total = area_lateral + area_base
latas_necessarias = area_total / 15




print(f"Area a ser pintada: {area_total:.2f}")
print(f"Quantidade de litros necessarios: {litros:.2f}")
print(f"A area da base é: {area_base:.2f}")

if latas_necessarias == 1:
    custo = 50
    

if latas_necessarias == 2:
    custo = 48
   
    

if latas_necessarias == 3:
    custo = 46

   
if latas_necessarias > 3:
    custo = 45

print(f"Custo total: {custo:.2f}")







    











