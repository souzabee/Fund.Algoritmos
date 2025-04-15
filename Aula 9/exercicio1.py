z = [0, 0, 0, 0]
while True:
    n = int(input("Digite numeros: "))
    
    if n < 0:
        break
    
    elif 0 <= z[0] <= 25:
        z[0] += 1
    elif 26 <= z[1] <= 50:
        z[1] += 1
    elif 51 <= z[2] <= 75:
        z[2] += 1
    elif 76 <= z[3] <= 100:
        z[3] += 1

print(z[0])
print(z[1])
print(z[2])
print(z[3])

