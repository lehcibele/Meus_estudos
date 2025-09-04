export function Acomodacao() {
    return (
        <div>
            <span>IMAGEM ACOMODAÇÃO</span>
            <h1>São Roque, Brasil</h1>
            <p>DES. Perto da vinícola Góes</p>
        </div>
    );
}

export function Menu() {
    return (
        <div>
            Acomodações | Experiências
        </div>
    );
}

interface CabecalhoProps {
    titulo: string;
    preco: string | number;
}

export function Cabecalho(props: CabecalhoProps) {

    return (
        <div className="bg-blue-700">
            <h1>Logo</h1>
            <p>{props.titulo}</p>
            <p>{props.preco}</p>
            <Menu />
        </div>
    );
}

