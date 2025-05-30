"""
    Exercicios com funções
        1 - Crie uma função que multiplica todos os argumentos não nomeados recebidos e retorne o total para uma variável e mostre o valor da variável.

        2 - Crie uma função fala se um número é par ou impar e retorne se o número é par ou impar
"""

# 1 
# numeros = []
# while True:
#     valor = int(input("Para sair[0] - Digite os números: "))
#     if valor == 0:
#         break
#     numeros.append(valor)

# def multiplica(*args):
#     total = 1
#     for valor in args:
#         total *= valor
#     return total

# resultado = multiplica(*tuple(numeros))
# print(f'A multiplicação dos números é: {resultado}')

# 2
numero = int(input("Digite um número: "))

def par_impar(num):
    if num % 2 == 0:
        return f'O número {num} é par'
    else:
        return f'O número {num} é impar'

res = par_impar(numero)
print(res)
