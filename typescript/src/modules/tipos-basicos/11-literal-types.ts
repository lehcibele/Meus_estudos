//let logType: string = 'info';
//logType = 'warn';

// aqui o tipo é a variável do tipo info
let logType: 'info';
// logType = 'warn'

// type alias
type LogType = 'info' | 'warn' | 'error';

export function logger(type: LogType, message: string) {
    switch(type){
        case 'info':
            console.log(`Info: ${message}`);
            break;
        case 'warn':
            console.log(`Warn: ${message}`);
            break;
        case 'error':
            console.log(`Erro: ${message}`);
            break;
    }
}

logger('error', 'log com alguma informação sobre o que houve!');