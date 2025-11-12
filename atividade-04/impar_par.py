def analisador_numeros():
    numeros_pares = 0
    numeros_impares = 0

    while True:
        try:
            entrada = input("Digite um numero inteiro ou sair para encerrar o programa: ")

            if entrada.lower() == 'sair':
                print("Analise Finalizada!")
                break

            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O Numero {numero} é par")
                numeros_pares += 1
            else:
                print(f"O Numero {numero} é ímpar")
                numeros_impares += 1
        except ValueError:
            print("Entrada invalida, por favor digite um numero inteiro")
            continue
    
    print("Resultado da Analise")
    print(f"Total de números pares: {numeros_pares}")
    print(f"Total de números ímpares: {numeros_impares}")

analisador_numeros()