// Usar pages é a maneira antiga de criar rotas, atualmente usamos a pasta src -> app -> e dentro de app fica as rotas (páginas), desse modo nem todos os arquivos de app vão ser rotas, já usando page todos os arquivos viram rotas

import '../../app/globals.css'

export default function Page() {
    return <h1 className="bg-red-500">Blog</h1>
}