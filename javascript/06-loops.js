/* 
    while(condição) {
        Executa entquanto a condição é verdadeira
    }
*/
let postagens = [
    "Hoje passando pela avenida paulista",
    "Passando por Natal",
    "Hoje fiz um curso",
    "Hoje é domingo"
];

const TotalPostagens = postagens.length;

let numero = 0;
while(numero < TotalPostagens) {
    console.log("IMAGEM" + numero);
    console.log(postagens[numero]);
    console.log("----");
    numero = numero + 1;
}

/* 
    do {
        faz uma primeira execução
        depois faz o teste
    }while(condicao)
*/
let numero2 = 5;
do {
    console.log("Executou " + numero2);
    numero2--;
}while(numero2 >= 1)

/* 
    for(inicialização; condição; incremento){
        comandos
    }
*/

for(let num = 1; num <= 5; num++) {
    console.log("Executou " + num);
}

/* 
    for variavel in array
*/

let postagens2 = [
    "Hoje passando pela avenida paulista",
    "Passando por Natal",
    "Hoje fiz um curso",
    "Hoje é domingo"
];

for(indice in postagens2) {
    console.log(postagens[indice]);
}