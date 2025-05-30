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
    latir() {
        console.log("Latir");
    }
}

class Passaro extends Animal { // subclasse - filho
    voar() {
        console.log("Voar");
    }
}

// Instancia
const cao = new Cao()
const passaro = new Passaro()



