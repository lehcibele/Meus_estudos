const estados = ["São Paulo", "Ceará", "Rio de Janeiro", "Bahia", "Minas Gerais"];

// ** Remover elementos do array **
//estados.pop()       // remove o último elemento
//estados.shift()     // remove o primeiro elemento

// ** Adiciona novo elemento no array **
//estados.push("teste")   // adiciona ao final
//estados.unshift("ttt")  // adiciona ao inicio

// ** Retorna novo array **
//const novo = estados.splice(0, 2);  // remove os elementos 0 e 1
//const novo1 = estados.splice(0, 2, "teste1", "teste2", "teste3"); // remove e adiciona novos itens

//console.log(novo1);     // fica salvo os elementos que foram removidos
//console.log(estados);

//const novo = estados.slice(0, 2);   // corta uma parte do array e retorna essa parte

// ** Converter Array -> string **
const usuarios = ["Jamilton", "Ana", "Carlos"];
let texto = usuarios.join();    // pega o array e converter em strings
let arrayTexto = texto.split(",");  // pega a string e converter em array

console.log(texto);
console.log(arrayTexto);