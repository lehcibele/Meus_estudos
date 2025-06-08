function processar(callbackSucesso, callbackErro) {
    // ações 
    let resultadoProcessamento = true;
    if(resultadoProcessamento) {
        callbackSucesso();
    }else {
        callbackErro();
    }
}

const salvarResultado = function() {
    // ações
    console.log("Salvar Resultado");
}

const erro = function() {
    // ações
    console.log("Erro");
}

processar(salvarResultado, erro);