// se o type não é aplicado, o type Any é inferido de modo implicito
// ao colocar file: any é tipado de modo explicito
export function handleFileUpload(file: any) {
    console.log(`Nome: ${file.name}`);
    console.log(`Tamanho: ${file.zise}`); // aqui da erro durante a execução, estoura um undefined
}

handleFileUpload({name: 'lista_de_funcionarios.txt'})