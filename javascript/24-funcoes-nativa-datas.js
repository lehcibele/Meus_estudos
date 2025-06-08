const data = new Date();

console.log(data.toString());    // converte a data em uma string
console.log(data.getDate());     // retorna o dia 
console.log(data.getMonth() + 1);   // retorna o mes (janeiro - 0, fevereiro - 1, ..., dezembro - 11), incrementa 1 para janeiro = 1
console.log(data.getFullYear());    // retorna o ano 

console.log(data.getHours());       // retorna a hora
console.log(data.getMinutes());     // retorna os minutos
console.log(data.getSeconds());     // retorna os segundos   

// Operações com datas
data.setDate(data.getDate() + 10); // setDate -> adiciona 30 dias
data.setMonth(data.getMonth() + 2); // setMonth -> adiciona 2 meses
data.setFullYear(data.getFullYear() + 1); // setFullYear -> adiciona 1 ano
let d = data.getDate();
let m = data.getMonth() + 1;
let a = data.getFullYear();
console.log(`data: ${d}/${m}/${a}`);

// operações com horas
data.setHours(data.getHours() + 2); // setHours -> adiciona 2 horas
data.setMinutes(data.getMinutes() + 20); // setMinutes -> adiciona 20 minutos
data.setSeconds(data.getSeconds() + 30); // setSeconds -> adiciona 30 segundos
let h = data.getHours();
let min = data.getMinutes();
let s = data.getSeconds();
console.log(`Hora: ${h}:${min}:${s}`);