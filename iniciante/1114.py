senha = 2002
senha_input = 20021
while senha_input != senha:
    senha_input = int(input())
    if senha_input != senha:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
