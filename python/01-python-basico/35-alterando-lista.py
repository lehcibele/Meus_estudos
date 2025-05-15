"""
    Listas em python
    Tipo list -> mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - indices e fatiamento
    Métodos úteis: 
        append, insert, pop, del, clear, extend, +, 
    Create Reade Update Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)

    Na lista é melhor adicionar/remover do final.
    Ao remover do começo/meio os valores vão ter que se descolados para a esquerda, aumentado o processamento.
"""

lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] # apaga o que está no indice 2 da lista
# print(lista)
# print(lista[2])

# Adicionar itens ao final da lista (append)
lista.append(50)
lista.append(60)
lista.append(70)
lista.append('Le')
print(lista)

# Remover o último item da lista (pop) -> retorna o valor
ultimo_valor = lista.pop()
print(lista, 'Removido ', ultimo_valor)

# Remover item pelo valor do indice
