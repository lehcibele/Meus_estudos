// let programmer: {name: string; age: number; skills: string[] } = {}
let programmer = {
    name: 'leticia',
    age: 25,
    skills: ['JavaScript', 'TypeScript'],
}

programmer.name = 'Levi';
programmer.age = 3

// O "?" diz que o atributo é opcional
export function showProgrammer(programmer: {name: string, age: number, skills?: string[]}) {
    console.log(programmer);
}

showProgrammer(programmer);
showProgrammer({name: 'lele', age: 31});