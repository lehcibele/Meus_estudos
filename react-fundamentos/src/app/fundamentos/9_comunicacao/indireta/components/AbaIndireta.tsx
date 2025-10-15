
interface AbaProps {
    atualizar(nome: string): void
}

export default function AbaIndireta(props: AbaProps){ // Pai

    return (
        <div>
            <button onClick={() => props.atualizar('Conversas')}>Conversas</button>
            <button onClick={() => props.atualizar('Atualizações')}>Atualizações</button>
            <button onClick={() => props.atualizar('Chamadas')}>Chamadas</button>
        </div>
    )
}