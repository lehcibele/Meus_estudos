const numeros = [2, 3, 5];

const resultado = numeros.reduce((acumulador, valor, i) => {
    //console.log("i: " + i);
    //console.log("ac: " + acumulador);
    //console.log("valor: " + valor);
    //console.log("-------");
    return acumulador + valor;
});

//console.log(resultado);

const produtos = [
    {nome: "Notebook", promocao: true},
    {nome: "Celular", promocao: false},
    {nome: "Mouse", promocao: true},
    {nome: "Celular", promocao: false},
];

const produtosPromo = produtos.map(produto => produto.promocao);

const novo = produtosPromo.reduce((acumulador, atual) => {
    return acumulador || atual;
});

if(novo) {
    console.log("Tem promoção");
} else {
    console.log("Não tem promoção");
}