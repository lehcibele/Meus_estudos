# Importe o módulo math e calcule a raiz quadrada de 64.
import math
print(math.sqrt(64))

# Crie um arquivo chamado calculadora.py com funções de soma, subtração, multiplicação e divisão.
    # Crie o arquivo chamado calculadora.py e criei as funções solicitadas

# Em outro arquivo, importe o módulo calculadora e use as funções.
import calculadora

soma = calculadora.soma(2, 2)
print(soma)
subtr = calculadora.subtracao(10, 5)
print(subtr)
mult = calculadora.multiplicacao(2, 3)
print(mult)
div = calculadora.divisao(9, 3)
print(div)

# Crie um pacote chamado meu_pacote com dois módulos:
    # saudacoes.py → função que cumprimenta pelo nome.
    # operacoes.py → função que calcula o quadrado de um número.

# Em outro arquivo, importe ambos os módulos do pacote e use as funções.
from meu_pacote_03 import saudacoes, operacoes
print(saudacoes.saudacao('Letícia'))
print(operacoes.numQuadrado(4))