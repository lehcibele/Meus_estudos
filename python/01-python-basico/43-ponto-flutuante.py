"""
    Double precisão
"""

import decimal # modulo decimal


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2)) # round(numero, casa decimais) -> arredonda o float no primeiro é o valor e o segundo ´número de casas decimais

# usa quando quer uma precisão muito grande
numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_4 + numero_5
print(numero_6)

