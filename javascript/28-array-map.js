// percorre todos os itens transformar o array em outro resultado
const pessoas = ["Ana", "Pedro", "Levi"];

let funcao = function(item, indice, arr) {
    //return "Olá " + item
    return {nome: item}
}

const novoArray = pessoas.map(funcao);

console.log(novoArray);

// 1 dolar = 3 reais
const produtosDolar = [
    {produto: "Notebook", preco: 1200, moeda: "$"},
    {produto: "Celular", preco: 800, moeda: "$"},
];

// const produtosReal = produtosDolar.map(function(item){
//     let preco = item.preco * 3;
//     return {produto: "Notebook", preco: preco, moeda: "R$"}
// });

const produtosReal = produtosDolar.map(item => {
    let preco = item.preco * 3;
    return {produto: "Notebook", preco: preco, moeda: "R$"}
})

console.log(produtosReal);