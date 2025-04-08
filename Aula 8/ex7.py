z =  [-10, -8, 0, 1, 2, 5, -2, -4]


print(max(z))
print(min(z))

soma_t = 0
for indice in range (len(z)):
    soma_t += z[indice]
    media = soma_t/8

print(media)