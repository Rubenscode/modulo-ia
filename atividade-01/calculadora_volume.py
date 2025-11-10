# Este programa calcula o volume de uma caixa retangular

# Solicita as dimensões da caixa ao usuario em cm
comprimento = int(input("Digite o comprimento da caixa: "))
largura = int(input("Digite a largura da caixa: "))
altura = int(input("Digite a altura da caixa: "))

# Calcula o volume da Caixa
volume = comprimento * largura * altura

# Exibe o Resultado
print(f"O volume da caixa é {volume} cm³")