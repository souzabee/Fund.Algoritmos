

nome = input('Digite o nome: ')

while nome != '':
    telefone = input('Digite seu telefone: ')
    contatos = open('contatos.txt', 'a')
    contatos.write(f'{nome} {telefone}\n')
    contatos.close()
    nome = input('Digite o nome: ')
    if nome and telefone == '':
        break
    
