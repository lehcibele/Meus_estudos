"""
    Introdução às funções (def) em python
    Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
    Elas podem receber valores para parâmetros(argumentos) e retorna um valor especifico.
    Por padrão, funções python retorna None (nada)
"""

# Se o argumento nome não tiver nenhum valor sendo passado, vai ser usado o 'Sem nome'
def saudacao(nome = 'Sem nome'): 
    print(f'Olá, {nome}!')

saudacao('Leticia')
print('----------------------')

"""
    Argumentos nomeados e não nomeados em funções Python:
        Argumentos nomeado tem nome com sinal de igual
        Argumentos não nomeado recebe apenas o argumento (valor)
"""

# x e y são parâmetros
def soma(x, y):
    print(f'{x=} {y=} | x + y = {x + y}')

soma(1, 2)
soma(y=1, x=2) # argumentos nomeados
print('----------------')

"""
    Valores padrão para parâmetros
    Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
    Refatorar: Editar o seu código
"""

# Caso o z não seja enviado para o parâmetro, é feito o bloco do else
def soma1(x, y, z = None):
    if z is not None:
        print(x + y + z) 
    else:
        print(x + y)

soma1(1, 2, 2)
soma1(3, 5, 2)
soma1(100, 200)
print('----------------------')

"""
    Escopo de funções em Python
    Escopo significa o local onde aquele código pode atingir.
    Existe o escopo global e local:
        O escopo global: 
            é o escopo onde todo o código é alcançavel.
        O escopo local:
            é onde apenas nomes do mesmo local podem ser alcançados.
"""
# escopo global
x = 1

def escopo():
    x = 10 # esse x é diferente do x de cima
    def outra_funcao():
        y = 2 
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print('----------------------')

"""
    Retorno de valores de funções (return)
"""

def soma2(x, y):
    return x + y
    print(1 + 1) # é inalcansavel, pois depois do return a função para

soma3 = soma2(2, 2)
soma4 = soma2(3, 3)
# print(soma3 + soma4) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType', não estava usando o return na função soma, estava usando o print, por isso deu esse erro
print(soma3 + soma4) # usando return na função soma