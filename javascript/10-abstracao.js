/* 
    Pilar 1 - Abstração
    Modelo (classe), entidade (objeto), identidade, caracteristicas() e ações
*/

// modelo -> nesse exemplo é o carro do uber
class Carro {
    constructor() {
        this.marca = "Volkswagen",
        this.modelo = "Gol",
        this.cor = "prata",
        this.placa = "EMJ-2565"
    }
    // método (ações)
    ligar() {

    }
}

// Instância da classe Carro -> o objeto carro é uma entidade
const carro = new Carro(); // identidade
carro.modelo = "Golf";
console.log(carro.modelo);

// identida -> os objetos tem identidades únicas
const carro2 = new Carro(); // identidade
console.log(carro2.modelo);

// loja virtual
class Produto {
    constructor() {
        // roupas
        this.tamanho = "M",
        this.cor = "Vermelho",
        this.preco = "45,90"

        // eletronicos
        this.altura = "50cm",
        this.largura = "30cm"
    }
}