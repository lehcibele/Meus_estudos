"""
    args -> Argumentos não nomeados
        * - *args (empacotamento e desempacotamento)
"""

# Lembrete de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    #print(args, type(args))

soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

outra_soma = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(outra_soma)

# print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13)))

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 # empacotamento
outra_s = soma(*numeros) # desempacota, pq na função soma está empacotando com o *args 
print(outra_s)