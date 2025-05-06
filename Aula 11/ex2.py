from random import randint

dicionario = {}

for _ in range (100):
    n = randint(0,20)
    if n not in dicionario:
        dicionario[n] = 1
    else: 
        dicionario[n] = dicionario[n] + 1

print(dicionario)
