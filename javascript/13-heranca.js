/* 
    Herança -> Reutilização e manutenção
    Classe -> Cao e Passaro
*/

class Animal { // superclasse - pai
    constructor(cor, tamanho, peso) {
        this.cor = cor,
        this.tamanho = tamanho,
        this.peso = peso
    }

    correr() {
        console.log("Correr");
    }

    dormir() {
        console.log("Dormir");
    }
}

class Cao extends Animal { // subclasse - filho
    constructor(cor, tamanho, peso, tamanhoOrelha) {
        super(cor, tamanho, peso),    // chama o constructor da classe Animal
        this.tamanhoOrelha = tamanhoOrelha
    }

    latir() {
        console.log("Latir");
    }
}

class Passaro extends Animal { // subclasse - filho
    voar() {
        console.log("Voar");
    }
}

//Papagaio herda de passaro que herda de animal
class Papagaio extends Passaro {
    falar() {
        console.log("Falar");
    }
}

// Instancia
const animal = new Animal("Amarelo", 60, 3) // passando parametros para o constructor animal
const cao = new Cao("Amarelo", 60, 3, 5);
const passaro = new Passaro();
const papagaio = new Papagaio();

console.log(cao.tamanho)

// console.log(animal.cor);

// papagaio.correr();
// papagaio.voar();
// papagaio.falar();

// cao.correr()
// passaro.correr();
// passaro.voar();
// passaro.cor = "Amarelo"
// console.log(passaro.cor);

