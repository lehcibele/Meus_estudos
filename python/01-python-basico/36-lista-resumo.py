"""
    Listas em python
    Tipo list -> mutável
    Na lista é melhor adicionar/remover do final.
    Ao remover do começo/meio os valores vão ter que se descolados para a esquerda, aumentado o processamento.
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - indices e fatiamento
    
    Métodos úteis: 
        append(valor) -> Adiciona um item ao final da lista 
        insert(index, valor) -> Adiciona um item no índice escolhido
        pop() pop(index) -> Remove um item ao final ou do índice escolhido
        del -> Apaga um indice
        clear -> Limpa a lista
        extend -> Estende a lista
        + -> Concatena listas
    
    Create Reade Update Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#........0...1...2...3
lista = [10, 20, 30, 40]

# Adiciona um item ao final da lista (append)
lista.append('Leticia')

# Remove o último item da lista (pop)
nome = lista.pop()
print(lista, nome)

# Apagar um indice (del)
    # Para apagar o último item da lista, sendo que eu não sei qual é o ultimo indice, faz: lista[-1]
#del lista[3]

# Insere um valor em um indice escolhido (inserted(indice, valor))
lista.insert(0, 5)
print(lista)

# Concatenando listas +
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # extend não retorna nada, está estendendo a lista a, alterando ela, colocando os valores da lista b na lista a
print(lista_c)
print(lista_a)