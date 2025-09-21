import { Acomodacao, Cabecalho, Conteudo, Menu, Rodape } from "@/components/interface";

export default function Page() {
    return (
        <div>
            <Cabecalho 
            titulo="AirBnb" 
            subtitulo="Minhas Acomodações"
            />

            <Menu />

            <Conteudo> 
                <h1>Página Início</h1>
                <p>
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Incidunt consequuntur voluptates illum cumque voluptatum fugiat amet ratione hic velit eaque! Accusantium repudiandae tempore corrupti dolorem voluptatibus. Error est quod laudantium.
                </p>
            </Conteudo>
            
            <Rodape />
        </div>
    );
}