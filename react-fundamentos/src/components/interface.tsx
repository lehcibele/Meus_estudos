import Link from "next/link";

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
        <div className="bg-gray-400">
            <MenuItem  texto="Home" url="/inicio"/>
            <MenuItem  texto="Acomodações" url="/acomodacoes"/>
            <MenuItem  texto="Ajuda" url="/inicio"/>
        </div>
    );
}

export function MenuItem(props: any) {
    return (
        <Link href={props.url} className="p-2">
            {props.texto}
        </Link>
    );
}

interface CabecalhoProps {
    titulo: string;
    subtitulo: string | number;
}

export function Cabecalho(props: CabecalhoProps) {

    return (
        <div className="bg-blue-200">
            <p>{props.titulo}</p>
            <p>{props.subtitulo}</p>
        </div>
    );
}

export function Rodape() {
    return(
        <div className="bg-blue-200">
            <p>Rodapé</p>
        </div>
    );
}

export function Conteudo(props: any) {
    // props.children -> mostra todos os filhos da tag Conteudo que está na pasta inicio.tsx
    return(
        <div className="bg-gray-200">
            {props.children}
        </div>
    );
}