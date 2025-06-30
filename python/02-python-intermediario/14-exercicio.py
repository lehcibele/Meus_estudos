"""
    Aumente os preços dos produtos a seguir em 10%
    Gere novos_produtos por deep copy (cópia produnda)
    Ordene os produtos por nome decrescente (do maior para o menor)
    Gere produtos_ordenadospor_nome por deep copy 
    Ordene os produtos por preco crescente (do menor para o maior)
    Gere produtos_ordenados_por_preco por deep copy

"""

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = [
    {**produto, 'preco': round(produto['preco'] + produto['preco'] * 0.10, 2) }
    for produto in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), reverse=True, key=lambda produto: produto['nome'])

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos),  key=lambda produto: produto['preco'])

print(*produtos, sep='\n')
print(40 * '-')
print(*novos_produtos, sep='\n')
print(40 * '-')
print(*produtos_ordenados_por_nome, sep='\n')
print(40 * '-')
print(*produtos_ordenados_por_preco, sep='\n')