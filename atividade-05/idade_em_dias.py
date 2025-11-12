import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano = int(input("Digite o seu ano de nascimento (Ex 1995): "))
idade_em_dias = calcular_idade_em_dias(ano)
print(f"Sua idade aproximada em dias é: {idade_em_dias} dias")

