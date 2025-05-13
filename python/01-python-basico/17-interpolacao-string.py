"""
Interpolação de string é o processo de inserir valores em uma string.
s -> string
d e i -> int 
f -> float
x e X -> hexadecimal (ABCDEF0123456789)
"""

nome = 'Leticia'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (15, 15)) # 04 é para preencher o restante do hexadecimal, caso não venha os 4