// 1º forma, com o primeiro botão é chamado no HTML
function executar() {
    console.log("Executar");
}

function executar2() {
    console.log("Executar2");
}


// 2º forma, é usado a função sem parenteses, pois se utilizar parenteses a função é executada mesmo sem clicar no elemento
// const botao = document.getElementById('botao');
// botao.onclick = executar;

// atributo personalizado 
const botao2 = document.querySelector('[botao-acao]');

// 3º forma, mas utilizado
const botao = document.getElementById('botao');
botao.addEventListener('click', function() {
    executar();
    executar2();
});