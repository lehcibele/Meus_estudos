// Funções construtoras para construir objetos

class Produto { 

}

const produto = new Produto();
console.log(typeof Produto);
console.log(typeof produto);

// criando classe usando função construtora - encapsulamento
const Hotel = function() {
    this.nome = 'Hotel',
    this.quantidadeSuites = 30,
    this.suitesOcupadas = 25,
    this.reservar = function() {
        if(this.suitesOcupadas < this.quantidadeSuites) {
            this.suitesOcupadas++;
            console.log("Ocupadas: " + this.suitesOcupadas);
        } else {
            console.log("Suites ocupadas");
        }
    }
}

const hotel = new Hotel();
hotel.reservar();