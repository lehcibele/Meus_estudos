// Tipando valores primitivos
type Salary = number | string;

// type alias foi criado para a tipagem de um objeto
type Programmer = {
    name: string, 
    age: number, 
    skills?: string[],
    contact: {email: string, phone: string},
    salary: Salary,
}

export function showProgrammer(programmer: Programmer) {
    console.log(programmer);
}

showProgrammer({
    name: 'lele',
    age: 31,
    contact: {email: 'leticia@gmail.com', phone: '84999999999'},
    salary: 1500,
});