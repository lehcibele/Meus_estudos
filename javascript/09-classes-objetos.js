// Notação literal
// const hotel = {
//     quartos: 20,
//     ocupados: 10,
//     piscinas: 2,
//     verificarDisponibilidade: function() {
//        let res = this.quartos - this.ocupados;
//        return "Disponíveis: " + res;
//     }
// }

// hotel.quartos = 25; // hotel['quartos'] = 25    outra notação
// //delete hotel.piscinas;    // apaga a propriedade
// console.log(hotel.piscinas);

// Notação de construtor (objeto em branco)
// const hotel = new Object();
// hotel.quartos = 20;
// hotel.ocupados = 10;
// hotel.verificarDisponibilidade = function() {
//     let res = this.quartos - this.ocupados;
//     return "Disponíveis: " + res;
// }
// console.log(hotel.quartos);
// console.log(hotel.verificarDisponibilidade());

// Criando classes
class Hotel {
    constructor() {
        this.quartos = 20
        this.ocupados = 10
    }

    verificarDisponibilidade() {
        let res = this.quartos - this.ocupados;
        return "Disponivel: " + res;
    }
}

// Instanciando a classe Hotel -> transforma em um objeto
const hotel = new Hotel();

console.log(hotel.verificarDisponibilidade());