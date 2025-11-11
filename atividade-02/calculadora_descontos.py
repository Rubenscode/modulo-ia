# Calculadora de desconto em uma loja

# Informações do Produto
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o valor do produto: "))
porcentagem_desconto = int(input("Digite a percentagem de desconto do produto: "))

# Calculo do desconto e do preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos Resultados
print(f"\nProduto: {nome_produto}")
print(f"Preço: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor Desconto: R$ {valor_desconto:.2f}")
print(f"Total com Descontos: R$ {preco_final:.2f}")