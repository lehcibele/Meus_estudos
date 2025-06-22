# List comprehension é uma forma rápida para criar listas a partir de iteráveis

import pprint

# print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)

# print(lista)

# criando a mesma lista com list comprehension
lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)

# Mapeamento  de dados com list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
# modificando o preço dos produtos
    # O que vem a esquerda do for é MAPEAMENTO (MAP)
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}   
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

# Filtrando
    # O que vem a direita do for é FILTRO
lista1 = [n for n in range(10) if n < 5]
print(lista1)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}   
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

print(*novos_produtos, sep='\n')