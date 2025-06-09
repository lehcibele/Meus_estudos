// objeto array
const frutas = new Array("morango", "banana");
console.log(typeof(frutas));

// literal
const nomes = ["Leticia", "Pedro"];
const numeros = [3, 2, 1];
// adiciona no final
nomes.push("Maria");
// deleta item
// delete nomes[2]
// alterar um item
nomes[2] = "Angelo"
console.log(nomes);

// método sort -> ordena os nomes
nomes.sort();
numeros.sort();

console.log(nomes);
console.log(numeros);

