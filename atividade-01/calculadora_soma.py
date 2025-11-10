# Este programa soma dois numeros inseridos pelo usuario

# Solicita ao usuario que insira dois numeros inteiros
numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite mais um numero inteiro: "))

# Calcula a soma dos numeros
soma = numero1 + numero2

# Exibe o resultado (Formatado com f-string)
print(f"A soma de {numero1} + {numero2} é: {soma}")