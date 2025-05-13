nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

contem_espaco = ' ' in nome

if len(nome) > 0 and idade > 0:  # uma outra forma é nome and idade
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if contem_espaco:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome)-1]}')
else:
    print('Desculpe, você deixou campos vazios')