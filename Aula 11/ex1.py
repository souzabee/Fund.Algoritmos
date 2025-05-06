dicionario = {
        'alpha': 1,
        'bravo': 2,
        'charlie': 1,
        'delta' : 3,
        'echo' : 1,
    }


def procuraChave (dicionario, valor):
    keys = []
    for key in dicionario:
        if dicionario[key] == valor:
            keys.append(key)
    print(keys)

procuraChave(dicionario, 1)
            

    
    
        

