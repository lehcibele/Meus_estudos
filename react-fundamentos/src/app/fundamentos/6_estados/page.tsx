// diretiva -> diz para o servidor que quer ser executado pelo próprio navegador do usuário e não pelo servidor
'use client'

import { useState } from "react";

export default function Page() {

    const [numero, setNumero] = useState(0);
    
    function incrementar() {
        setNumero(numero + 1)
        console.log("número: " + numero);
    }

    function decrementar() {
        setNumero(numero - 1)
        console.log("número: " + numero);
    }
    
    return (
        <div>
            <h1>Estados</h1>
            <button 
            onClick={incrementar}
            className="bg-blue-500 p-2 mr-2"
            >
                Incrementar
            </button>

            <button 
            onClick={decrementar}
            className="bg-blue-500 p-2"
            >
                Decrementar
            </button>

            <p>Número: {numero}</p>
        </div>
    );
}
