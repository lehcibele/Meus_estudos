# Crie uma função que receba um nome e retorne "Olá, [nome]!".
def saudacao(nome):
    return f"Olá, {nome}!"
saudacao('Leticia')

# Crie uma função que receba dois números e retorne a multiplicação entre eles
def multiplicacao(num1, num2):
    return num1 * num2
res = multiplicacao(2, 3)
print(res)

# Crie uma função que receba uma lista de números e retorne a soma total
def soma_total(*args):
    total = sum(args)
    return total 
print(soma_total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Crie uma função com parâmetros opcionais que mostre uma frase com seu nome e idade. Se não informadas, use "Visitante" e 0.
def apresentacao(nome='visitante', idade=0):
    return f"Meu nome é {nome} e tenho {idade} anos"
print(apresentacao())

# Crie uma função que aceite qualquer quantidade de números e retorne o maior valor
def maior_com_max(*numeros):
    return max(numeros)
print(f"Maior usando o max: {maior_com_max(0, -2, -19, 23, 22, 56, 100, 21, 3, 44)}")
print(f"Maior usando o max: {maior_com_max(-5, -2, -9)}")

def maior_numero(*numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero >= maior:
            maior = numero
    return maior
print(f'Maior usando if: {maior_numero(0, -2, -19, 23, 22, 56, 100, 21, 3, 44)}')    
print(f'Maior usando if: {maior_numero(-5, -2, -9)}')    


# Crie uma função que aceite dados pessoais como nome, idade e cidade usando **kwargs e exiba esses dados
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

dados_pessoais(nome='leticia', idade=25, curso='Eng. de Computação')
    
# Crie uma função chamada menor_numero que receba qualquer quantidade de números e retorne o menor valor entre eles
def menor_numero(*numeros):
    menor = numeros[0]
    for numero in numeros:
        if numero <= menor:
            menor = numero
    return menor 

print(f'O menor número é: {menor_numero(4, 6, 1, 2, 3, 7)}')
print(f'O menor número é: {menor_numero(-8, -2, -4, -1, 4, 5)}')

# Crie uma função chamada contar_pares que receba qualquer quantidade de números e retorne quantos deles são pares
def conta_pares(*numeros):
    total_par = 0
    for numero in numeros:
        if numero % 2 == 0:
            total_par += 1
    return total_par

print(f"O total de números pares é: {conta_pares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")

# Crie uma função chamada soma_impares que receba uma lista de números e retorne a soma de todos os números ímpares dessa lista
def soma_impares(numeros):
    soma_numero_impar = 0
    for numero in numeros:
        if numero % 2 != 0:
            soma_numero_impar = soma_numero_impar + numero

    return soma_numero_impar
print(f"O total de números impares é: {soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")

    