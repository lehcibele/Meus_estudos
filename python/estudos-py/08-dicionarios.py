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


    