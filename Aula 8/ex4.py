z = []

for n in range (10):
    num = int(input("Digite um numero: "))
    z.append(num)
print(f"Numeros: {z}")

sp = 0
si = 0
for num in z:
    if num % 2 == 0:
        sp += num
        
for indice in range(len(z)):
    if indice % 2 == 0:
        si += z[indice]
            

        
print(f"Soma numeros pares: {sp}")
print(f"Soma dos indices pares: {si}")      
        

