y = 0
soma  = 0
for notas in range (9):
    y = y + 1
    soma = notas + soma
    notas = int(input("Digite as notas: "))
    if 10 < notas < 0:
        break
    
    media = soma/y
if notas >= 6:
    print ("Alunos aprovados:", y)
print(media)

