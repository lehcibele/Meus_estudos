'use client'
import { useState } from "react";

// imc = peso / (altura * altura)
// < 18 -> abaixo do peso
// 18 e 25 -> peso normal
// > 25 -> sobrepeso

export default function CalculadoraIMC() {
    
    const [peso, setPeso] = useState('');
    const [altura, setAltura] = useState('');
    const [resultado, setResultado] = useState('');
    
    function calculoImc(){
        const pesoNum = parseFloat(peso);
        const alturaNum = parseFloat(altura);

        if(pesoNum <= 0 || alturaNum <=0 ){
            setResultado("Informe valores válidos");
        } else {
            setResultado("");
        }
        
        const imc = pesoNum / (alturaNum * alturaNum);
        let categoria = "";

        if(imc <= 18){
            categoria = "Abaixo do Peso";
        } else if(imc > 18 && imc <= 25) {
            categoria = "Peso normal";
        } else {
            categoria = "Sobrepeso";   
        }

        setResultado(`IMC: ${imc.toFixed(2)} - ${categoria}`);
    }
    
    return (
        <div className="container-imc">
            <h1 className="border-b-1">Cálculo IMC</h1>
            <br />

            <label>Digite seu peso</label>
            
            <br />

            <input 
                type="text"
                placeholder="Ex: 90"
                className="campo-texto"
                value={peso}
                onChange={(e) => setPeso(e.target.value)}
            /> KG

            <br />
            
            <label>Digite sua altura</label>

            <br />

            <input 
                type="text"
                placeholder="Ex: 1.70"
                className="campo-texto"
                value={altura}
                onChange={(e) => setAltura(e.target.value)}
            /> Metros

            <br />
            <br />

            <button className="botao" onClick={calculoImc}>Calcular</button>
            <h2>Resultado: {resultado}</h2>
        </div>
    );
}