/*
    Como atribuir um objeto a uma constante e depois fazer alterações nessa constante
*/

let produto = {
    nome: "Notebook"
}

produto = {
    nome: "Celular"
}

// produto = { // erro, uma constante não pode ser alterada
//     nome: "Celular"
// } 
console.log(produto.nome);