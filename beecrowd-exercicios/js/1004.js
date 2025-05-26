/* 
    Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.   

    Entrada
    O arquivo de entrada contém 2 valores inteiros.

    Saída
    Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
*/

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let numero1 = parseInt(lines[0]);
let numero2 = parseInt(lines[1]);
let PROD = numero1 * numero2;
console.log(`PROD = ${PROD}`);