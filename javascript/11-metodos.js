/*
    Métodos - retornos e parâmetros
*/

class Usuario {
    constructor() {
        this.email = "",
        this.senha = "",
        this.subtotalCompra = 0
    }

    logar() {
        let emailBD = "ja@gmail.com";
        let senhaBD = "1234";

        if(senhaBD == this.senha) {
            //console.log("Senha válida");
            return "Senha válida";
        } else {
            //console.log("Senha inválida");
            return "Senha inválida";
        }
    }

    calcularDesconto(cupom) {
        let desconto = 0;
        if(cupom == "DESC20"){
            desconto = 20;
        } else if (cupom == "FESTA10") {
            desconto = 10;
        }

        return this.subtotalCompra - desconto;

        
    }
}

const usuario = new Usuario();
usuario.email = "ja@gmail.com";
usuario.senha = "12345"

let retorno = usuario.logar()
console.log(retorno);

// operação de calculo de compra com cupom de desconto
usuario.subtotalCompra = 500;
let totalcompra = usuario.calcularDesconto("DESC20");
console.log(totalcompra);

