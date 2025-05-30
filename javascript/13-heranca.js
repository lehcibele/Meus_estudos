/* 
    Herança -> Reutilização e manutenção
    Classe -> Cao e Passaro
*/

class Animal { // superclasse - pai
    constructor() {
        this.cor = "",
        this.tamanho = 0,
        this.peso = 0
    }

    correr() {
        console.log("Correr");
    }

    dormir() {
        console.log("Dormir");
    }
}

class Cao extends Animal { // subclasse - filho
    constructor() {
        super(),    // chama o constructor da classe Animal
        this.tamanhoOrelha = 0
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
const cao = new Cao();
const passaro = new Passaro();
const papagaio = new Papagaio();

papagaio.correr();
papagaio.voar();
papagaio.falar();

// cao.correr()
// passaro.correr();
// passaro.voar();
// passaro.cor = "Amarelo"
// console.log(passaro.cor);

