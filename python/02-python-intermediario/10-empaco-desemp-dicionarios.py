# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# acessa a chave 
a, b = pessoa
print(a, b)
print()
# acessa os valores
a, b = pessoa.values()
print(a, b)

# desempacotamento interno
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)
print()

dados_pessoa = {
    'idade': 16,
    'altura': 1.60,
}

# Juntar dicionarios pessoa e dados_pessoa
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

