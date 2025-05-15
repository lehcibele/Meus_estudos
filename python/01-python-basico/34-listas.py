"""
    Listas em python
    Tipo list -> mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - indices e fatiamento
    Métodos úteis: append, insert, pop, del, clear, extend
"""
#........+01234
#........-54321
string = 'ABCDE' # 5 caracteres (len)

# Formas de declarar uma lista
lista = list() 
# lista = [] # lista vázia

#.........0...1......2................3....4
#........-5...-4......-3.............-2...-1
lista = [123, True, 'Leticia Cibele', 1.2, []]  
print(lista[2], type(lista[2]))

# Alterando um item da lista
lista[-3] = 'João' # lista[-3] == lista[2]
print(lista)
print(lista[2], type(lista[2])) 