nome = 'Leticia Cibele'

tamanho_da_string = len(nome)

print(nome)
print(tamanho_da_string)

nova_string = ''

contador = 0

while contador < tamanho_da_string:
    nova_string += f'*{nome[contador]}'
    contador += 1

print(nova_string)