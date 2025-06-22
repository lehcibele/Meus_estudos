let shoppingCart = [200.75, 150.12, '33.90', '44', 'not defined'];
//let total: string | number;

//export function totalize(values: Array<string | number>)
export function totalize(values: (number | string)[]) { // retornar o total
    return values
        .map(value => typeof value === 'number' ? value : parseFloat(value)) // converter todos os valores para números
        .filter(value => !isNaN(value))// Filtrar valores validos
        .reduce((acc, curr) => acc + curr, 0) // totalizar
}

console.log(totalize(shoppingCart));