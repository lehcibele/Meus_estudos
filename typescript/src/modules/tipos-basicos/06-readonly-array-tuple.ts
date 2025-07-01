// readonly impede que seja alterado os valores do array
// let numbers: readonly number[] = [10, 20, 30, 40, 50];
let numbers: ReadonlyArray<number> = [10, 20, 30, 40, 50];

let numbers1: readonly [number, number, number, number, number] = [10, 20, 30, 40, 50];

// erro por conta que foi usado o readonly que é só para leituras
// numbers[0] = 30;

let numbersCopy = numbers.map(item => item * 2);

console.log(numbers);
console.log(numbersCopy);

export default () => {}