"""
Fatiamento de Strings
    [i:f:p] [::]
    OBS: A função len retorna a quantidade de caracteres de uma string.
"""

variavel = 'Olá mundo'
print(variavel[4:])  # Retorna a partir do índice 4 até o final da string
print(variavel[4:8]) # Retorna do índice 4 até o índice 8 (não inclui o índice 8)
print(variavel[:4])  # Retorna do início da string até o índice 4 (não inclui o índice 4)
print(variavel[-8:-2]) # Retorna do índice -8 até o índice -2 (não inclui o índice -2)

print(len(variavel)) # Retorna a quantidade de caracteres da string

print(variavel[0:len(variavel):2]) # Retorna do índice 0 até o final da string, pulando de 2 em 2 caracteres