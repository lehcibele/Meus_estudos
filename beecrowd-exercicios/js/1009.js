/* 
    Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

    Entrada
    O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

    Saída
    Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
*/

let nomeVendedor = 'JOAO';
let salarioFixo = 500.00;
let totalVendas = 1230.30;
let comissao = 0.15;
let salarioTotal = salarioFixo + (totalVendas * comissao);
console.log(`TOTAL = R$ ${salarioTotal.toFixed(2)}`);