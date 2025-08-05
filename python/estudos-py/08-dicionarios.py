# 1️⃣ Cadastro de Pessoa
# Crie um dicionário chamado pessoa com as chaves:
# "nome", "idade", "email"
# Peça para o usuário preencher esses dados usando input() e depois imprima

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
email = input("Digite seu email: ")

pessoa = {
    "Nome": nome,
    "Idade": idade,
    "Email": email   
}

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# 2️⃣ Contador de Palavras
# Dado um texto (frase digitada pelo usuário), conte quantas vezes cada palavra aparece usando um dicionário.
frase = input("Digite uma frase; ")
palavras = frase.split() # split() -> transforma a frase em uma lista de palavras
print(palavras)

contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print("\nContagem de palavras:")
for palavra, quantidade in contador.items():
    print(f"{palavra}: {quantidade}")

