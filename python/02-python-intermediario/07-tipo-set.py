"""
    Sets - Conjuntos em python (tipo set)
    Sets em python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

    Criando um set
        set(iterável) ou {1, 2, 3}

    Sets são eficientes para remover valores duplicados de iteraveis:
        Não aceitam valores mutáveis (list, dict, set, bytearray);
        Seus valores são sempre únicos;
        eles não tem índexes, não podem acessar elementos por posição;
        eles não garantem ordem;
        eles são iteráveis (for, in, not in)

    Métodos úteis:
        add, update, clear, discard

    Operadores úteis:
        união | união (union) - Une
        intersecção & (intersection) -> Itens presentes em ambos
        diferença - -> itens presente apenas no set da esquerda
        diferença simétrica ^ -> itens que não estão em ambos
    
    Quando usar set?
        Remover duplicatas de uma lista (converter a lista para set primeiro);
        Testar se um valor pertence;
        Operações matemáticas, como união, intersecção

"""

# Criando um set vázio
# s1 = set()
# print(s1, type(s1))

# Criando um set com um valor - o set itera sobre o valor, mas não garante a ordem
# s2 = set('Leticia')
# print(s2)

# Criando um set com dados
# s3 = {'Leticia', 1, 2, 3}
# print(s3)

# Set elimina valores duplicados
# s1 = {1, 2, 3, 3, 3, 3, 3, 1}
# print(s1)

# Lista sendo convertida em um set para remover valores duplicados
# l1 = [1, 2, 3, 3, 3, 3, 3, 1, 4, 4]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# verifica se um valor está no set
# s1 = {1, 2, 3}
# print(3 in s1)
# print(3 not in s1)
# print(4 in s1)

# for numero in s1:
#     print(numero)

# Métodos
s1 = set()
s1.add('Leticia') # add - adiciona somente um por vez
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))    # manda vários valores
# s1.clear()  # limpa o clear
s1.discard('Olá mundo')     # remove 
#print(s1)

# Operadores
s2 = {1 , 2, 3}
s3 = {2, 3, 4}
s4 = s2 | s3
s4 = s2 & s3
s4 = s2 - s3    # itens presentes apenas no set da esquerda
s4 = s2 ^ s3
print(s4)

# Remover duplicatas de uma lista:
lista = [1, 2, 2, 3, 4, 4]
unicos = set(lista)
print(unicos)  # {1, 2, 3, 4}

# Testar pertencimento com rapidez:
nomes = {"Ana", "Carlos", "João"}
print("Ana" in nomes)  # True

# Operações matemáticas (interseção, união etc.):
python = {"Letícia", "Carlos", "Ana"}
javascript = {"Carlos", "Pedro"}

comuns = python & javascript
print(comuns)  # {'Carlos'}

