let nome = "carro de leticia";

console.log(nome.length);                         // tamanho da string nome
console.log(nome.charAt(1));                      //  localiza o caractere pela posição
console.log(nome.replace("leticia", "pedro"));    // substitui a string, não altera a string nome
console.log(nome);

let frase = "O sucesso é ir de fracasso em fracasso sem perder o entusiasmo";
console.log(frase.substring(2, 4));

// separa string, se não for passado o separador, por padrão é o espaço
let nome2 = 'leticia-cibele';
let resultado = nome2.split("-");
console.log(resultado);

