// type inference
// let filmes = ['Duna: Parte 2', 'Divertida mente 2'];
// declarando um tipo array de strings
// let filmes: string[] = ['Duna: Parte 2', 'Divertida mente 2'];
// declarando um tipo array de numeros
//let numbers: number[] = [10, 20];
// outra forma de declarar um tipo array usando type annotation convencional
let filmes: Array<string> = ['Duna: Parte 2', 'Divertida mente 2'];
// outra forma de declarar um tipo array usando type annotation convencional
let numbers: Array<number> = [10, 20];

export function toUpperCaseStrings(arr: string[]) {
    return arr.map(value => value.toUpperCase());
}

console.log(toUpperCaseStrings(filmes));