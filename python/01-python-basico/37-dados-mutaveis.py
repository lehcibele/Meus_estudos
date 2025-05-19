"""
    Cuidados com dados mutáveis:
        Copiado o valor (imutáveis)
        Aponta para o mesmo valor na memória (mutável)
"""

# Lista_b aponta para o mesmo endereço de memória da lista_a, se eu altero a lista_a também vai alterar a lista_b
lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy() # Ao usar o .copy(), não aponta mais para o mesmo endereço da memória, é feito uma copia

lista_a[0] = 'Qualquer coisa'

print(lista_a)
print(lista_b)

