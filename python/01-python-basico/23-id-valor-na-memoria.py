"""
    Flag (bandeira) - Marca um local
    None = não valor
    is e is not = é ou não é (tipo, valor, identidade)
    id = identidade
"""

# as duas variáveis abaixo estão apontando para o mesmo objeto na memória
v1 = 'a' 
v2 = 'a'
print(id(v1))
print(id(v2))