// Descendentes de Object
const obj = {}

//console.log(obj.toString());
//console.log(obj.__proto__ == Object.prototype);

class Carro {
    constructor() {
        this.placa = "AMP-1230"
    }
}

class Bmw extends Carro {
    constructor() {
        super(),
        this.nome = "BMW 320i"
    }
}

// const objBmw = new Bmw();
// console.log(objBmw.placa);
// console.log(objBmw.nome);

// Prototype chain -> encadeamento de objetos
const veiculo = {
    motor: "50 cavalos"
}

const carro = {
    placa: "AMP-1230",
    __proto__: veiculo,
    acelerar: function(){
        console.log("Acelerar");
    }
}

const bmw = {
    nome: "BMW 320i", 
    motor: "300 cavalos",
    __proto__: carro    // estabele uma relação de herança com carro, usando prototipo 
}

console.log(bmw.motor);
bmw.acelerar();

