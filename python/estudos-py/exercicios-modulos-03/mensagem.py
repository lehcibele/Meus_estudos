# 2️⃣ Exercício — Módulo de Mensagens Personalizadas
# Crie um módulo chamado mensagens.py com uma função que:
    # Recebe um nome e um horário do dia (manhã, tarde, noite);
    # Retorna uma saudação personalizada.
# Teste o módulo em outro arquivo com exemplos de manhã, tarde e noite.

def saudacao(nome, horario):
    if horario < 12:
        return f"Bom dia {nome}"
    elif horario < 18:
        return f"Boa tarde {nome}"
    else:
        return f"Boa noite {nome}"