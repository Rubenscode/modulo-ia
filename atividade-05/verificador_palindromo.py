def palindromo(texto):
    texto_limpo = ''.join(letra.lower() for letra in texto if letra.isalnum())
    return texto_limpo == texto_limpo[::-1]

entrada = input("Digite uma palavra ou frase: ")
palindromo = palindromo(entrada)

if palindromo == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"{entrada} é um palindromo? {resposta}")