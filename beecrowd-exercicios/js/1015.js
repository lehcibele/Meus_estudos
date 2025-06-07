/*
    Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

    Distancia = raiz( (x2- x1)^2 + (y2 - y1)^2 )

    Entrada
    O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

    Saída
    Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.
*/

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let [x1, y1] = lines[0].split(' ');
let [x2, y2] = lines[1].split(' ');

x1 = parseFloat(x1);
y1 = parseFloat(y1);
x2 = parseFloat(x2);
y2 = parseFloat(y2);

distancia = Math.sqrt( Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2) );

console.log(`${distancia.toFixed(4)}`);