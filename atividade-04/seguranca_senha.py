def verifica_senha():
    while True:
        senha = input("Digite uma senha ou ('sair' para encerar o programa):")

        if senha.lower() == 'sair':
            print("Programa Encerrado!")
            break

        if len(senha) < 8:
            print("Por Questoes de segurança digite uma senha com no minimo 8 caracteres")
            continue

        if not any(letra.isdigit() for letra in senha):
            print("Por questoes de segurança sua senha deve conter pelo menos um numero")
            continue

        print("Senha forte e valida!")
        break

verifica_senha()