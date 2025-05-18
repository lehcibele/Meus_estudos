"""
    Iterável -> str, range, etc
    Iterador -> quem sabe entregar um valor por vez
    next -> me entregue o próximo valor
    iter -> me entregue seu iterador
"""

# texto = iter('Leticia') # __iter__()

# # print(texto.__next__())
# print(next(texto)) # texto.__next__()
# print(next(texto))
# print(next(texto))

# for letra in texto
# texto = 'Leticia'
# iterador = iter(texto)

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará...')
        break
    
    for j in range(1, 3):
        print(i, j)
else:    
    print('For completo com sucesso!')