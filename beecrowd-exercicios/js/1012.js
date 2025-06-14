/*
    Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
    a) a área do triângulo retângulo que tem A por base e C por altura.
    b) a área do círculo de raio C. (pi = 3.14159)
    c) a área do trapézio que tem A e B por bases e C por altura.
    d) a área do quadrado que tem lado B.
    e) a área do retângulo que tem lados A e B.

    Entrada
    O arquivo de entrada contém três valores com um dígito após o ponto decimal.

    Saída
    O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
*/

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const PI = 3.14159;

let [a, b, c] = lines[0].split(' ');

a = parseFloat(a);
b = parseFloat(b);
c = parseFloat(c);

// area triangulo
let areaTriangulo = a * c / 2;
// area circulo
let areaCirculo = PI * Math.pow(c, 2);
// area trapezio
let areaTrapezio = ((a + b) * c)/2;
// area quadrado
let areaQuadrado = Math.pow(b, 2);
// area retangulo 
let areaRetangulo = a * b

console.log(`TRIANGULO: ${areaTriangulo.toFixed(3)}`);
console.log(`CIRCULO: ${areaCirculo.toFixed(3)}`);
console.log(`TRAPEZIO: ${areaTrapezio.toFixed(3)}`);
console.log(`QUADRADO: ${areaQuadrado.toFixed(3)}`);
console.log(`RETANGULO: ${areaRetangulo.toFixed(3)}`);
