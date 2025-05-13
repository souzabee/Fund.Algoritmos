from random import randint

with open('numeros.txt', 'w') as arquivo:
    for i in range(100):
        arquivo.write(f'{randint(0, 100)} ')

def somar_numeros(arquivo):
    with open(arquivo, 'r') as arq:
        numeros = arq.read().strip().split()
        soma = sum([int(num) for num in numeros])

    return soma

print(somar_numeros('numeros.txt'))