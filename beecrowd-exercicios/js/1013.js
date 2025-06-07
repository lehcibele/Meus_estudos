/* 

    MaiorAB = (a + b + abs*(a-b))/2

    Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

    Entrada
    O arquivo de entrada contém três valores inteiros.

    Saída
    Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
*/

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let [a, b, c] = lines[0].split(' ');

a = parseInt(a)
b = parseInt(b)
c = parseInt(c)
let maior = 0;
if((a > b) && (a > c) ){
    maior = a;
} else if(b > c){
    maior = b;
} else {
    maior = c;
}

console.log(`${maior} eh o maior`);