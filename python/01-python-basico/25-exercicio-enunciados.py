"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um inteiro.
"""

# num = input('Digite um número inteiro: ')

# if num.isdigit():
#     num_int = int(num)
#     if num_int % 2 == 0:
#         print(f'O número {num_int} é par')
#     else:
#         print(f'O número {num_int} é ímpar')
# else:
#     print(f'O número {num} não é um inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horario descrito, exiba uma saudação aproprieada. Ex:
Bom dia 0-11,, Boa tarde 12-17, Boa noite 18-23
"""

# hora = input('Digite a hora (0 - 23): ')

# try: 
#     hora_int = int(hora)
#     if hora_int >= 0 and hora_int <= 11:
#         print('Bom dia!')
#     elif hora_int >= 12 and hora_int <= 17:
#         print('Boa tarde!')
#     elif hora_int >= 18 and hora_int <= 23:
#         print('Boa noite!')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')