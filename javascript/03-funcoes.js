/* 
    1) desligar torneira;
    2) pedir copo de água;
    3) Ir ao mercado comprar arroz;
*/

// function desligarTorneira() {
//     console.log("Desligar torneira");
// }

// desligarTorneira();

// function pedirCopoAgua() {
//     return "Copo Água";
// }

// let retorno = pedirCopoAgua();
// console.log(retorno)

// function irMercadoComprarArroz(dinheiro) {
//     console.log("Pegar Transporte");
//     console.log("Procurar Arroz");

//     return "arroz";
// }

// let retorno = irMercadoComprarArroz(10);
// console.log(retorno);

function calcularMedia(nota1, nota2) {
    let totalNotas = nota1 + nota2;
    let media = totalNotas / 2;

    return media;
}

let media = calcularMedia(9, 8);
console.log(media);