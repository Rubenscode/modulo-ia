# Calculadora de consumo de combustivel

# Solicitar os Dados da Viagem
distancia_percorrida = int(input("Digite a distancia percorrida em km: "))
combustivel_gasto = int(input("Digite a quantidade de combustivel em litros: "))

# Calculo do consumo
consumo = distancia_percorrida / combustivel_gasto

# Exibição do Resultado
print(f"\n Dados da Viagem:")
print(f"Distancia Percorrida: {distancia_percorrida} km")
print(f"Combustivel Gasto: {combustivel_gasto} Litro(s)")
print(f"Consumo Medio: {consumo:.2f} km/l")