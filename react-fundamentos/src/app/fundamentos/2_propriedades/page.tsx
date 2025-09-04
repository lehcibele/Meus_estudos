import { Acomodacao, Cabecalho } from "@/components/interface";

export default function Page() {
    return (
        <div>
            <Cabecalho 
            titulo ="São Roque, Brasil"
            preco="R$ 350"
            />
            <hr />
            <Acomodacao />
            <Cabecalho 
            titulo ="Campos do Jorddão, Brasil"
            preco="R$ 500"
            />
            <hr />
            <Acomodacao />
        </div>
    );
}