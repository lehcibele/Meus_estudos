export default function Page() {
    const usuarios = [
        {id: "1", nome: "Leticia", email: "l@gmail.com"},
        {id: "2", nome: "Pedro", email: "p@gmail.com"},
        {id: "3", nome: "Carol", email: "c@gmail.com"},
        {id: "4", nome: "Josivaldo", email: "j@gmail.com"},
        {id: "5", nome: "Simão", email: "s@gmail.com"},
    ];

    const lista = usuarios.map( usuario =>
        <li key={usuario.id}>
            { usuario.nome } ( { usuario.email } )
        </li>
    );

    return (
        <ul>
            {lista}
        </ul>
    );
}