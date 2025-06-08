// Parâmetros padrão
// function somar(numero1, numero2){
//     numero1 = isNaN(numero1) ? 0 : numero1;
//     numero2 = isNaN(numero2) ? 0 : numero2;

//     return numero1 + numero2;
// }

// valor padrão do es2015
function somar(numero1 = 0, numero2 = 0) {
    return numero1 + numero2;
}

console.log(somar(2));  // NaN -> Not a Number (não é um número)

// Parâmetros e retornos opcionais
function calcularSalario(salario, desconto) {
    //desconto = isNaN(desconto) ? 0 : desconto
    if(salario == 0) {
        console.log("Salario não informado");
        return 0;
    } else {
        return salario - desconto;
    }
    
}

let resultado = calcularSalario(100, 20);
console.log(resultado);
