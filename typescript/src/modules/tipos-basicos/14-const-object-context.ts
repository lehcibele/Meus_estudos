type File = {
    name: string,
    size: number
}
// const file = {
//     name: 'lista_de_funcionarios.txt',
//     size: 456123789,
// } as const // deixa os atributos do objeto somente para leitura (readonly)

const file: File = {
    name: 'lista_de_funcionarios.txt',
    size: 456123789,
}

file.name = 'lista_de_dependentes.txt' // como foi usado as const não é possivel alterar o atributo, pois dá erro

export function handleFileUpload(file: any) {
    console.log(`Nome: ${file.name}`);
    console.log(`Tamanho: ${file.zise}`); // aqui da erro durante a execução, estoura um undefined
}

handleFileUpload(file);