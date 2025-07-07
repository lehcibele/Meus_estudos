# 3️⃣ Exercício — Pacote de Operações Financeiras
# Crie um pacote chamado financas com os módulos:
    # descontos.py: função que calcula o preço com desconto.
    # juros.py: função que calcula o valor com juros simples.
# Depois, em outro arquivo:
    # Importe ambos os módulos e:
    # Calcule o preço de R$100 com 15% de desconto;
    # Calcule o valor de R$500 aplicando 2% ao mês por 6 meses.

def func_juros(valor):
   jurosPorMes = (valor * 0.02) * 6
   jurosFinal = valor + jurosPorMes
   return f"{jurosFinal:.2f}"