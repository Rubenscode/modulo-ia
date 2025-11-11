def calculadora():
    while True:
        try:
            numero1 = float(input("Digite o primeiro numero: "))
            numero2 = float(input("Digite o segunddo numero: "))
            operacao = input("Digite a operação desejada (+ - * /): ")

            if operacao == '+':
                resultado = numero1 + numero2
            elif operacao == '-':
                resultado = numero1 - numero2
            elif operacao == '*':
                resultado = numero1 * numero2
            elif operacao == '/':
                resultado = numero1 / numero2
            else:
                print("Operação Invalida!")
        except ValueError as e:
            print(f"Erro: {e}. Tente Novamente")
        except ZeroDivisionError:
            print("Invalido: Divisão por zero não é permitida. Tente Novamente!")
        else:
            print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")

calculadora()