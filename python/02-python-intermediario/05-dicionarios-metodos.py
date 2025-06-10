"""
    len -> quantas chaves
    keys -> iterável com as chaves
    values -> iterável com os valores
    items -> iterável com chaves e valores
    setdefault -> adiciona valor se a chave não existe
    copy -> retorna uma cópia rasa (shallow copy)
    get -> obtem uma chave
    pop -> apagar um item com a chave especificada (del)
    popitem -> apaga o último item adicionado
    update -> atualiza um dicionário com outro
"""

import copy     # para usar o deepcopy (copia profunda)

pessoa = {
    'nome': 'Leticia',
    'sobrenome': 'Cibele',
}

pessoa.setdefault('idade', None) # adiciona a chave idade um valor

#print(len(pessoa))            # pessoa.__len__()
#print(list(pessoa.keys()))    # imprime as chaves e converte p/ lista
#print(list(pessoa.values()))  # imprime os valores e converte p/ lista
#print(list(pessoa.items()))   # imprime as chaves e valores
#print(pessoa['idade'])

# for chave in pessoa.keys():   # imprime as chaves
#     print(chave)

# for valor in pessoa.values(): # imprime os valores
#     print(valor)

# for chave, valor in pessoa.items():  # imprime a chave e valor
#     print(chave, valor)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# d2 aponta para o mesmo endereço de d1, como alterou d2, d1 foi alterado também, pois o dicionario é mutável
# d2 = d1
# d2['c1'] = 1000
# print(d1)

# para copiar, usa copy -> copy não entra no subnivel, então a lista não vai ser copiado, vai ser alterado
d2 = copy.deepcopy(d1)  # entra em todos o ssuniveis 
d2['c1'] = 100
d2['l1'][1] = 9999
# print(d1)
# print(d2)

p1 = {
    'nome': 'Leticia',
    'sobrenome': 'Cibele',
}

# print(p1['nome'])
# print(p1.get('nome', 'Nome não existe')) # pega o valor da chave nome, se a chave não existe, impremi nome não existe

# nome = p1.pop('nome')   # apaga a chave nome
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()   # apaga a última chave
# print(ultima_chave)
# print(p1)

# atualiza chaves e cria novas chaves
# p1.update({ 
#     'nome': 'novo valor',
#     'idade': 25
# })

# p1.update(nome='novo valor', idade = 30) # outra forma de criar o update

# tupla = ('nome', 'novo valor'),
# p1.update(tupla)

lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)