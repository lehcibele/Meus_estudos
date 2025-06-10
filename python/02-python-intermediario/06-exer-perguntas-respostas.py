# Exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
resposta_correta = False

print(f'Pergunta: {perguntas[0]['Pergunta']}?')
print('')
print("Opções: ")

for index, opcao in enumerate(perguntas[0]['Opções']):
    print(f'{index}) {opcao}')

resp_1 = int(input("Escolha uma opção: "))

for index, opcao in enumerate(perguntas[0]['Opções']):
    if perguntas[0]['Resposta'] == opcao:
        indice = index
        if resp_1 == index:
            resposta_correta = True
            acertos += 1
            break  

if resposta_correta:
    print("Acertou 👍")
    resposta_correta = False
else:
    print("Errou ❌")

print('')
print(f'Pergunta: {perguntas[1]['Pergunta']}?')
print('')
print("Opções: ")

for index, opcao in enumerate(perguntas[1]['Opções']):
    print(f'{index}) {opcao}')

resp_2 = int(input("Escolha uma opção: "))

for index, opcao in enumerate(perguntas[1]['Opções']):
    if perguntas[1]['Resposta'] == opcao:
        indice = index 
        if resp_2 == indice: 
            resposta_correta = True
            acertos += 1
            break

if resposta_correta:
    print("Acertou 👍")
    resposta_correta = False
else:
    print("Errou ❌")

print('')
print(f'Pergunta: {perguntas[2]['Pergunta']}?')
print('')
print('Opções:')

for index, opcao in enumerate(perguntas[2]['Opções']):
    print(f'{index}) {opcao}')

resp_3 = int(input("Escolha uma opção: "))

for index, opcao in enumerate(perguntas[2]['Opções']):
    if perguntas[2]['Resposta'] == opcao:
        indice = index 
        if resp_3 == indice:
            resposta_correta = True
            acertos += 1
            break

if resposta_correta:
    print("Acertou 👍")
    resposta_correta = False
else:
    print("Errou ❌")

print('')
print(f'Você acertou {acertos} de 3 perguntas.')