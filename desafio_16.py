codigo_usuario = int(input("Digite o código do usuário: "))

if codigo_usuario != 1234:
    print("Usuário inválido!")
else:
    senha = int(input("Digite a senha: "))
    if senha != 9999:
        print("Senha incorreta!")
    else:
        print("Acesso permitido.")