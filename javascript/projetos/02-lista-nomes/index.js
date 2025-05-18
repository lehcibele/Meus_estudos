let nomes = [
    "jose",
    "leticia",
    "maria",
    "carlos",
    "carla",
    "marcela",
    "pedro",
    "jamilton",
    "carlos"
];

const btnCarregar = document.getElementById('btnCarregar');
const btnPesquisar = document.getElementById('btnPesquisar');

btnCarregar.addEventListener('click', carregarNomes);
btnPesquisar.addEventListener('click', pesquisarNome);

function carregarNomes() {

    let itensLista = '';

    for(indice in nomes){
        let nome = nomes[indice];
        itensLista += `<li class="list-group-item">${nome}</li>`;
    }

    document.getElementById('lista').innerHTML = itensLista;
}

function pesquisarNome() {
    const nomePesquisa = document.getElementById('inputNome').value;

    let itensLista = '';

    for(indice in nomes) {
        let nome = nomes[indice];
        if(nomePesquisa == nome){
            itensLista += `<li class="list-group-item">${nome}</li>`
        }
    }

    document.getElementById('lista').innerHTML = itensLista;
}