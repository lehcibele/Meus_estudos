"""
    Flag (bandeira) - Marca um local
    None = não valor
    is e is not = é ou não é (tipo, valor, identidade)
    id = identidade
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if is None)  # True
print(passou_no_if is not None)  # False