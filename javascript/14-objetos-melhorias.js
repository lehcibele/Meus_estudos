// Objetos literias - melhorias
let nome = "Notebook";
let preco = 1200;

// const produto = {
//     nome,   // nome: nome -> o js já criar a variável nome (simplifica)
//     preco,  // preco: preco
//     exibirProduto: function() {
//         console.log(`${this.nome}, ${this.categoria}`);
//     }
// }

class Produto {
    constructor() {
        this.nome = "Notebook",
        this.preco = 1200
    }
}

const produto = new Produto();
const pro = produto;
pro.preco = 2000;
produto.preco = 3000;
console.log(pro.preco);
console.log(produto.preco);

// Se fizer desse jeito, pro aponta para o mesmo endereço da memória de produto, então altera o preco do produto também
// const pro = produto; 
// pro.preco = 2000;
// console.log(pro.preco);
// console.log(produto.preco);

// produto.categoria = "Eletronicos";      // adicionando um novo atributo
// produto.exibirPreco = function () {     // adicionando um novo metodo
//     console.log(`Preço: ${this.preco}`);
// }

// console.log(produto.categoria);

// produto.exibirPreco();
// // console.log(produto.nome);