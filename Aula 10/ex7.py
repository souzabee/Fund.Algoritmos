from random import randint, random
notas = []
for num_linha in range (10):
    aluno = []
    for num_coluna in range (3):
        aluno.append(randint(0, 10))
    notas.append(aluno)

for aluno in notas:
    for notas in aluno:
        print(f'{notas:2d}', end = ' ')
    print()
for aluno in notas:
    min = min(aluno)
    prova = aluno.index(min)
    print(f'Aluno {notas.index(aluno)} - Prova {prova} - Nota {min}')






for prova in notas_transposta:




    

