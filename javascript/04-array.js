/* 
    Array -> Estrutura de dados usada para armazenar uma coleção ordenada de elementos.
        * Coleções podem ser dos tipos: números, strings, objetos, booleanos e arrys

    Métodos úteis de arrays:
        map() -> cria um novo array com base em outro
        filter() –> filtra elementos com base em uma condição
        reduce() –> reduz o array a um único valor
        find() –> retorna o primeiro elemento que satisfaz a condição
        includes() –> verifica se contém um valor
        indexOf() –> retorna o índice de um elemento
        sort() –> ordena os elementos
        reverse() –> inverte a ordem dos elementos
*/

// Declarando um array
let nomes = [];
let frutas = ['maça', 'banana', 'laranja'];
let mistos = ['texto', 10, true, [1, 2]];   // não é uma boa prática usar vários tipos no mesmo array

// Acessando elementos
console.log(frutas[0]);
console.log(frutas[2]);
// console.log(frutas[5]); // undefined 

// Modificando elementos
frutas[0] = 'morango'
console.log(frutas);

// Adicionar elementos ao final -> push()
nomes.push('Leticia');
nomes.push('Levi');
console.log(nomes);

// Adiciona elementos no inicio -> unshift()
nomes.unshift('Maria');
nomes.unshift('Carlos');
console.log(nomes);

// Apagar elementos -> delete
// delete nomes[0];
// console.log(nomes);

// Remove elemento ao final -> pop()
nomes.pop();
console.log(nomes);

// Remove elemento no inicio -> shift()
nomes.shift();
console.log(nomes);

// Remove, substitui ou adiciona elementos -> splice()
nomes.splice(1, 1, 'Levi');
nomes.splice(0, 1, 'Carlos', 'Pedro'); 
console.log(nomes);

// Tamanho do array
console.log(nomes.length);

// Percorre o array
frutas.forEach( fruta => {
    console.log(fruta);
});

// Usando alguns métodos
let numeros = [1, 2, 3, 4, 5];

let dobrados = numeros.map(n => n * 2); // [2, 4, 6, 8, 10]
let pares = numeros.filter(n => n % 2 == 0); //[2, 4]
let soma = numeros.reduce( (acc, n) => acc + n, 0); // 15
console.log(soma);
