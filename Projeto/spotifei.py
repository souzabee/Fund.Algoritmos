menu = {
    1 : 'Login',
    2 : 'Cadastre-se'
}

def main ():
    while True:
        escolha = interface()
        
        if escolha == 1:
            login()
            print('Voltando ao menu...\n')
        elif escolha == 2:
            cadastro()
            print('Voltando ao menu...\n')
    



def interface():
    print('Menu: ')
    for opcao, descricao in menu.items():
        print(f'{opcao} - {descricao}')
    
    escolha =  int(input('Escolha uma opção: '))
    
    return escolha

def login ():
    username_login = input("Insira seu username: ")
    senha_login = input("Insira sua senha: ")
    
    with open('user_data.txt', 'r') as arquivo:
        usuarios = arquivo.readlines()
    
    for linha in usuarios:
        username, senha = linha.strip().split(', ')
        if username_login.lower() == username.lower() and senha_login.lower() == senha.lower():
            print(f'Login realizado com sucesso, {username}!')
            return
       
    
    

def cadastro ():
    username = input("Crie seu username: ")
    senha = input("Crie sua senha: ")
    
    with open('user_data.txt', 'a') as arquivo:
        arquivo.write(f"{username}, {senha} \n")
        print("Cadastro realizado com sucesso!")
    
    


if __name__ == "__main__":
    main() 







































