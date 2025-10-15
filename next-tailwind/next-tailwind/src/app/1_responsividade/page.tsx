/*
    - sm -> 640px
    - md -> 768px
    - lg -> 1024px
    - xl -> 1280px
    - 2xl -> 1536px
*/

export default function Responsividade() {
    return (
        <div>
            <h1 
            className="
            bg-slate-300 
            md:bg-orange-300
            lg:bg-blue-800
            xl:bg-yellow-300
            2xl:bg-purple-900
            ">
                Responsividade
            </h1>
        </div>
    );
}