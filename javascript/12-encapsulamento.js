/* 
    Pilar - Encapsulamento
    Definição: Esconder detalhes da implementação, dando mais segurança a sua aplicação. O encapsulamento serve para controlar o acesso aos atributos e métodos de uma classe.
*/

class Carro {
    constructor() {
        this.modelo = "Gol",
        this.cor = "Vermelho"
    }

    frear() {
        /* 
            Freio com tecnologia a disco
            .
            .
        */
        console.log("Parar o carro");
    }
}

const carro = new Carro();
carro.frear();

// Encapsulamento, modificadores de acesso e getters e setter
class ContaBancaria {
    constructor() {
        // private, protected e public -> modificadores de acesso (em js não tem), usamos o _ ou # para a pessoa não acessar diretamente a propriedade
        this._numeroConta = 80,
        this._saldo = 0
    }

    sacar(valorSaque) {
        this._saldo = this._saldo - valorSaque;
    }

    depositar(valorDeposito) {
        this._saldo = this._saldo + valorDeposito;
    }

    // método getters (recuperar)
    get numeroConta() {
        // verificar se o usuario está logado
        return "Número: " + this._numeroConta;
    }

    // método setter (configurar valor)
    set numeroConta(numero) {
        if( numero > 0) {
            this._numeroConta = numero;
        }

    }

    get saldo() {
        return this._saldo;
    }

    set saldo(novoSaldo) {
        if(novoSaldo > 0) {
            this._saldo = novoSaldo;
        }
    }

}

const conta = new ContaBancaria();
//conta.numeroConta = 50;
//console.log(conta.numeroConta);

conta.saldo = 500;
conta.sacar(50);
conta.depositar(100);

console.log(conta.saldo);
