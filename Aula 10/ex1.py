from random import randint, random

inteiros = [(randint(0,10)) for _ in range(10)]
reais = [random () * 10 for _ in range(5)]
strings = ['a', 'b', 'c','d','e','f','g']
completa = [inteiros, reais, strings]

print(completa)
