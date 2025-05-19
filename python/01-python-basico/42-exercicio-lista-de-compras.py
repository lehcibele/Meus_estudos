"""
    Faça uma lista de compra com listas
    O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
    Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls' if os.name == 'nt' else 'clear') # limpa o terminal, cls -> windows, clear -> linux
        valor = input('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível apagar este índice')
    elif opcao == 'l':
        os.system('cls'  if os.name == 'nt' else 'clear') # limpa o terminal

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')