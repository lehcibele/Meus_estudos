"""
    Função lambda -> É uma função anônima que contém apenas uma linha.
"""

lista = [4, 32, 1, 34, 5, 6, 6, 21,]
lista.sort() # ordena crescentemente
lista.sort(reverse=True) # ordena decrescentemente
# print(lista)

lista_nomes = [
    {'nome': 'Luiza', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Isabel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# ordena os nomes usando o nome, para ordena no sobreno usa ['sobrenome']
def ordena(item):
    return item['nome']

# lista_nomes.sort(key=ordena) # passa a função, mas sem executar, ou seja, sem o ()

# Outra forma de ordenar, usando a função lambda
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista_nomes, key=lambda item: item['nome']) # expressão lambda, ordena do mesmo jeito que a linha decima
l2 = sorted(lista_nomes, key=lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)


