# 1️⃣ Crie uma lista com 5 números e:
    # Imprima a soma dos elementos;
    # Imprima o maior e o menor número;
    # Imprima os números ordenados.

lista_numeros = [25, -5, 34, 12, -4]

def operacoes_com_listas_sem_métodos(lista_num):
    maior = lista_num[0]
    menor = lista_num[0]
    soma = 0
    # Soma os números sem usar sum()
    for numero in lista_num:
        soma += numero
    #print('A soma dos números é: ', soma)
    # Imprime o maior número
    for numero in lista_num:
        if maior <= numero:
            maior = numero
        if numero < menor:
            menor = numero
    #print(f"O maior número é {maior} e o menor número é {menor}")
    # Imprime os numeros ordenados
    lista_ordenada = sorted(lista_num)
    #print(f"Lista ordenada: {lista_ordenada}")

operacoes_com_listas_sem_métodos(lista_numeros)

# 2️⃣ Crie uma lista de compras e:
    # Adicione um item com append;
    # Remova um item com remove;
    # Mostre o total de itens com len().
import math

menu = """
    [1] - Adicione um item a lista.
    [2] - Remova um item da lista.
    [3] - Mostre a lista completa.
    [0] - Sair.
""" 

print(menu)

def relatorio_lista_compras(lista):
    while True:
        opcao = input(" Escolha uma opção: ").strip()

        # Verifica se é string vazia
        if opcao == "":
            print("Valor inserido inválido.")
            continue

        # Tenta converter para número
        try:
            opcao = int(opcao)

            # Verifica se é NaN
            if math.isnan(opcao):
                print("Valor inválido.")
                continue
            # Converte para int se for inteiro
            opcao = int(opcao)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if opcao == 1:
            item = input('Adicione um item: ')
            lista.append(item)        
            print(f'{item.title()} foi adicionado com sucesso!')
        elif opcao == 2:
            item_removido = input('Qual item deseja remover? ')
            lista.remove(item_removido)
            print(f'{item_removido.title()} removido com sucesso!')
        elif opcao == 3:
            if len(lista) == 0:
                print('Lista vázia, adicione itens a lista!')
            for indice, item in enumerate(lista, start=1):
                print(f'{indice} - {item.title()}')
        elif opcao == 0:
            print('Lista de compras finalizado!')
            break
        else:
            print('Opção escolhida inválida')
               
lista_compras = []
relatorio_lista_compras(lista_compras)

# 3️⃣ Crie uma lista de nomes e:
    # Mostre os nomes em ordem alfabética;
    # Conte quantas vezes um nome aparece;
    # Inverter a ordem da lista.     

lista_nomes = ['leticia', 'ana', 'julia', 'carol', 'ana', 'ana']

lista_ordem_alfabetica = sorted(lista_nomes)
quantas_vezes_ana_aparece = lista_nomes.count('ana')
lista_invertida = lista_nomes[::-1]
print(f'Lista ordenada: {lista_ordem_alfabetica}\nQuantas vezes ana aparece: {quantas_vezes_ana_aparece}\nLista invertida: {lista_invertida}')


# 4️⃣ Crie uma função que receba uma lista de números e:
    # Retorne apenas os números pares;
    # Retorne a média dos valores.

lista_numeros2 = [1, 2, 3, 4, 5, 6, 7, 8]

def ope_com_numeros(lista):
    numeros_pares = [n for n in lista if n % 2 == 0]
    media_valores = sum(lista)/len(lista)
    return f'números pares: {numeros_pares}\n média dos valores {media_valores:.2f}'

print(ope_com_numeros(lista_numeros2))

# 5️⃣ Desafio: Crie uma matriz 3x3 usando listas aninhadas e exiba ela no formato de tabela.
matriz_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Exibindo como tabela
print("Matriz 3x3:")
for linha in matriz_3x3:
    for elemento in linha:
        print(f"{elemento:^5}", end=' ')  # centraliza com espaço
    print()  # pula para a próxima linha
    
        