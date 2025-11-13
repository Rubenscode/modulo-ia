import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    rua = dados['logradouro']
    bairro = dados['bairro']
    cidade = dados['localidade']
    estado = dados['uf'] 
    return f"Cep: {cep}\nRua: {rua}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}"

cep = input("Digite o CEP:")
print(consultar_cep(cep))
