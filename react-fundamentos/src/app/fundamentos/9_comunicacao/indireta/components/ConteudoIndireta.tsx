import AbaIndireta from "./AbaIndireta";
import { useState } from "react";

export default function ConteudoIndireta() {

    const [aba, setAba] = useState('');

    function alterarNome(nome: string) {
        setAba(nome);
    }

    return (
        <div>
            <span>{aba}</span>

            <hr />

            <AbaIndireta atualizar={alterarNome}/>
        </div>
    )
}