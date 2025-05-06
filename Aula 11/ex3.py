dicionario = {

}

from random import randint
def dados():
    for _ in range (1000):
        d1 = randint(1,6)
        d2 = randint(1,6)
        dados = d1 + d2
        if dados not in dicionario:
            dicionario[dados] = 1
        else:
            dicionario[dados] =+ 1
    return dados


