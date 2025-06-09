const usuarios = [
    {nome: "Jamilton", idade:32},
    {nome: "Ana", idade: 16},
    {nome: "Maria", idade:40}
];

const funcao = function(item, i, arr) {
    if(item.idade >= 18){
        return true;
    } else {
    return false
    }
}

const usuariosMaiorIdade = usuarios.filter(funcao);
//console.log(usuariosMaiorIdade);

const carros = [
    {nome: "Gol", marca: "volkswagem"}, 
    {nome: "iX35", marca: "hyundai"},
    {nome: "Santa Fé", marca: "Hyundai"},
    {nome: "Polo", marca: "volkswagem"},
];

const marcaHyndai = carros.filter(item => {
    // toLowerCase é usado para converte a string para minusculo e comparar
    return item.marca.toLowerCase() == "hyundai";
});

console.log(marcaHyndai);