"""
    Dicionários em Python (tipo dit)
    
    Dicionários são estruturas de dados do tipo par de "chave" e valor.
    
    Chaves podem ser consideradas como índice, que vimos na lista e podem ser de tipos imutáveis, como: str, int, floar, bool, tuple...
    
    O valor pode ser de qualquer tipo, incluindo outro dicionário.
    
    Usamos as chaves {} ou a classe dict para criar dicionários.
    
    Imutáveis: str, int, float, bool, tuple
    Mutável: dict, list

    pessoa = {
        'nome': 'Leticia',
        'sobrenome': 'Cibele',
        'idade': 25,
        'altura': 1.6,
        'endereco': [
            {'rua': 'tal tal', 'numero': 123},
            {'rua': 'outra rua', 'numero': 321},
        ]
    }
"""

# outra forma de criar o dicionário, menos usado
# pessoa = dict(nome='leticia', sobrenome='cibele')

pessoa = {
    'nome': 'Leticia',
    'sobrenome': 'Cibele',
    'idade': 25,
    'altura': 1.6,
    'endereco': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

# adicionando chave e valor
pessoa['apelido'] = 'leh' 

# criando chave dinamicamente
chave = 'cor'
pessoa[chave] = 'amarelo'

# Apagando a chave
del pessoa['cor']

# Evitar erro, caso a chave não existe
if pessoa.get('cor') is None:
    print('Não existe')
else:
    print(pessoa['cor'])

print()
print(pessoa)