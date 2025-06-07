"""
    Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

    Distancia = raiz( (x2- x1)^2 + (y2 - y1)^2 )

    Entrada
    O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

    Saída
    Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.
"""
import math

x1, y1 = input('').split(' ')
x2, y2 = input('').split(' ')

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = math.sqrt( pow((x2 - x1),2) + pow((y2- y1), 2) )
print(f'{distancia:.4f}')