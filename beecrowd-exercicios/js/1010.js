/* 
    Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

    Entrada
    O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

    Saída
    A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
*/

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let [codigo_peca1, num_peca1, valor_peca1] = lines[0].split( ' ');
let [codigo_peca2, num_peca2, valor_peca2] = lines[1].split(' ');

codigo_peca1 = parseInt(codigo_peca1);
num_peca1 = parseInt(num_peca1);
valor_peca1 = parseFloat(valor_peca1);

codigo_peca2 = parseInt(codigo_peca2);
num_peca2 = parseInt(num_peca2);
valor_peca2 = parseFloat(valor_peca2);

let total_peca1 = num_peca1 * valor_peca1;
let total_peca2 = num_peca2 * valor_peca2;

let total = total_peca1 + total_peca2;

console.log(`VALOR A PAGAR: R$ ${total.toFixed(2)}`);
