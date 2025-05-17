const btnNovaFrase = document.getElementById('btn-nova-frase');

btnNovaFrase.addEventListener('click', gerarFrase);

function gerarFrase() {
    const frases = ['Frase 1', 'Frase 2', 'Frase 3', 'Frase 4', 'Frase 5', 'Frase 6 ', 'Frase 7', 'Frase 8', 'Frase 9', 'Frase 10' ];
    const numeroAleatorio = Math.floor(Math.random() * 10);
    const frase = frases[numeroAleatorio];

    document.getElementById('frase').innerHTML = frase;
}


