export default function Tipografia() {
    return (
        <div>
            <h1 className="font-sans">Título 01</h1>
            <h1 className="font-serif">Título 02</h1>
            <h1 className="font-mono text-[2rem]">Título 03</h1>
            <h1 className="text-2xl">Título 04</h1>
            <h1 className="
            text-[1rem] 
            md:text-[2rem]
            lg:text-[3rem]
            xl:text-[4rem]
            ">
                Título 05
            </h1>

            <h1 className="italic">Título 06</h1>
            <h1 className="font-thin">Título 07</h1>
            <h1 className="font-thin tracking-wider">Título 08</h1>

            <h1 className="text-left">Esquerda</h1>
            <h1 className="text-center">Centro</h1>
            <h1 className="text-right">Direita</h1>
            

        </div>
    );
}