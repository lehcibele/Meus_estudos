# 1️⃣ Exercício — Módulo de Conversão de Temperatura
import conversor 
print(conversor.celsiusFahren(30))
print(conversor.fahrenCelsius(80))

# 2️⃣ Exercício — Módulo de Mensagens Personalizadas
import mensagem
print(mensagem.saudacao('Leticia', 15))
print(mensagem.saudacao('Levi', 19.25))

# 3️⃣ Exercício — Pacote de Operações Financeiras
from financas import desconto, juros
print(desconto.func_desconto(100))
print(juros.func_juros(500))

# 4️⃣ Exercício — Pacote de Utilitários
# from utilitarios import strings, listas
# lista_com_duplicatas = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]
# print(strings.inverterString('Letícia'))
# print(listas.removeDuplicatas(lista_com_duplicatas)) # [1, 2, 3, 4, 5, 6]

# 5️⃣ Exercício — Importação com Alias (Apelido)
# Usando o pacote financas criado no exercício 3:
# Importe os módulos descontos e juros usando apelidos (as).
# Refatore o código para usar os apelidos.
import utilitarios.listas as ls
import utilitarios.strings as st
lista_com_duplicatas = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]
print(st.inverterString('Letícia'))
print(ls.removeDuplicatas(lista_com_duplicatas))