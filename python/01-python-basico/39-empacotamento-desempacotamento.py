nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

# Se tiver mais valores do que variaveis, vai dar erro, caso contrário também
# nomes1 = ['Maria', 'Helena', 'Luiz']
# nome11, = nomes
# print(nome11)

# Para atribuir somente a uma váriavel, para não da erro usa uma variavel de resto
nomes1 = ['Maria', 'Helena', 'Luiz']
nome11, *_ = nomes1
print(nome11, _)

# Para pegar o segundo valor
_, nome22, *_ = nomes1 
print(nome22)

# Empacotamento e desempacotamento em funções
lista = ['Maria', 'Eduarda', 1, 2, 3, 'Helena']

for nome in lista:
    print(nome, end = ' ')

print(' ')
# Faz o mesmo que o for
print(*lista)