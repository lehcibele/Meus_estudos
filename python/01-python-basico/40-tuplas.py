"""
    Tupla -> uma lista imutável
    Para criar uma tupla, é só não usar colchetes
"""

nomes = 'Maria', 'Helena', 'Luiz'
# nomes = ('Maria', 'Helena', 'Luiz')
# nomes[1] = 'Outro' # Não pode alterar o valor na tupla, da erro

# Para converter uma lista em uma tupla, usa tuple()
nomes1 = ['Maria', 'Helena', 'Luiz']
nomes_tupla = tuple(nomes)
print(nomes)
