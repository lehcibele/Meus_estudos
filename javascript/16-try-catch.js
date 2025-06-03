// Tratamento de erros com Try Catch
function contarQuantidadeLetras(produto){
    try{
        console.log(produto.nome.length);
        console.log("Teste");
    }
    catch(erro) {
        tratarErro(erro)
        //console.log("Erro ao processar, código: 164");
    } /* finally {
        console.log('Finally');
    } */

    function tratarErro(erro) {
        throw new Error("Teste");
    }
}

const produto = {
    nom: 'Notebook',
    preco: 1200
}

contarQuantidadeLetras(produto)