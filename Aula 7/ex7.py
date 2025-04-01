sexo = input("Informe seu sexo: ")
peso = int(input("Informe seu peso: "))

def doacao(sexo, peso):
    if peso > 60 and sexo == "Homem":
        return True
    if peso > 50 and sexo == "Mulher":
        return True
    else:
        return False
    
apto = doacao(sexo, peso)
if apto:
    print('Voce esta apto')
else:
    print('VOce nao esta apto')

 


    
    

