"""
    split e join com list e str
    split -> divide uma string
    join -> une uma string
"""

frase = 'Olha só, que coisa interessante'
lista_palavras = frase.split()
lista_frases_cruas = frase.split(',')
print(lista_palavras)
print(lista_frases_cruas)

lista_frases = []

# strip() corta o espaço do começo e do fim
# rstrip() corta o espaço da direita
# lstrip() corta o espaço da esquerda
for i, frase in enumerate(lista_frases_cruas):
    #print(lista_frases[i].strip()) 
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases)

# Unir frases -> join()
frases_unidas = '-'.join(lista_frases)
print(frases_unidas)