import Image from "next/image";

export default function Page() {

    const usuario = {
        nome: "Ana Maria",
        urlPerfil: "https://domineia.com/wp-content/uploads/2023/02/inteligencia-artificial-fotos.jpeg"
    }

    return (
        <div>
            <h1>Imagem</h1>
            <Image 
                src={usuario.urlPerfil}
                alt="Foto usuário"
                width={90}
                height={90}
            />
            <Image 
                src="/img/tanjiro.jpeg"
                alt="Foto usuário"
                width={90}
                height={90}
            />
            
        </div>
    );
}