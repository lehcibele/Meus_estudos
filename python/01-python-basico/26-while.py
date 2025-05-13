"""
Repetições
While  (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
break -> Para o loop

Operadores de atribuição
= += -= *= /= //= **= %=
"""
# contador = 0

# while contador < 100:
#     contador += 1

#     if contador == 6:
#         print('Pulou o número 6')
#         continue

#     print(contador)

#     if contador == 40:
#         break
    
# print('Acabou')

qtd_linhas = 5 
qtd_colunas = 5 

linha = 1
while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')