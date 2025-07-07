# 1️⃣ Exercício — Módulo de Conversão de Temperatura
# Crie um módulo chamado conversor.py com funções para:
    # Converter Celsius para Fahrenheit;
    # Converter Fahrenheit para Celsius.
# Depois, em outro arquivo:
# Importe o módulo e use as funções para converter:
# 30°C para Fahrenheit;
# 86°F para Celsius.

def celsiusFahren(celsius):
    farenheit = (celsius * 1.8) + 32
    return f"O valor de {celsius} em celsius é {farenheit:.2f} em farenheit"

def fahrenCelsius(faren):
    celsius = (faren - 32) / 1.8
    return f"O valor de {faren} em farenheit é {celsius:.2f} em celsius"