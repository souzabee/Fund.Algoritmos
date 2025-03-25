primos = 0
n = int(input("Digite a qtde de numeros a serem testados: "))
for i in range (n):
    x = int(input("Digite o número: "))
    if x > 1 and x % x == 0:
        primos = primos + 1
    

print(f"voce digitou {primos:.0f} números primos")

    