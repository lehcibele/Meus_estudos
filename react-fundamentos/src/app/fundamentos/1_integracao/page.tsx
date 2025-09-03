export default function Page() {

    const regra = <h1>Maior de idade</h1>;
    const nome = "Leticia Cibele";

    const lista = [
        <h1 key="ana">Ana</h1>,
        <h1 key="pedro">Pedro</h1>,
        <h1 key="leticia">Leticia</h1>,
    ];

    const salario = 1000;
    const bonus = 200;

    const usuario = {
        nome: "Leticia",
        idade: "25",
    }

    function MeuBotao() {
        return (
            <button>Clique</button>
        )
    }

    return (
        <div id={nome}>
            Olá, {lista[0]}
            O salário é: {salario + bonus}
            O usuário é: {usuario.nome} idade: {usuario.idade}
            <MeuBotao />
        </div>
    );
}