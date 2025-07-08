# 1️⃣ Crie uma função que receba um texto e retorne:
    # Texto sem espaços nas bordas;
    # Texto em maiúsculas;
    # Quantidade de palavras (usando split).

def transforma_texto(texto):
    novo_texto = texto.strip().upper()
    quantidade_palavras = len(texto.strip().split())
    return f"Novo texto: {novo_texto} o texto possui essas plavras: {quantidade_palavras} "

print(transforma_texto("Esse é um texto de exemplo para treinar strings avançadas"))

# 2️⃣ Crie uma função que receba uma string e:
    # Retorne a string invertida;
    # Retorne quantas vezes a letra 'a' aparece (maiúscula ou minúscula);
    # Retorne True se a string for um palíndromo (mesmo ao contrário).

def string_invertida(frase):
    frase_invertida = frase[::-1]
    quantidade_de_a = frase.lower().count('a')
    eh_palindromo = frase.lower() == frase_invertida.lower()
    return f"String invertida: {frase_invertida.lower()}\nQuantas vezes a aparece: {quantidade_de_a}\nÉ palindromo: {eh_palindromo}"

print(string_invertida("Radar"))

# 3️⃣ Peça ao usuário para digitar uma frase e retorne:
    # A frase com cada palavra capitalizada (usar .title());
    # A frase centralizada com largura de 50 espaços, preenchida com '-'.

#fr = input('Digite uma frase: ')

def mudar_frase(frase):
    frase_capitalizada = frase.title()
    frase_centralizada = f"{frase:-^50}"
    return f"{frase_capitalizada}\n{frase_centralizada}"

#print(mudar_frase(fr))

# 4️⃣ Crie uma função que formate um preço decimal, mostrando:
    # Duas casas decimais;
    # O preço alinhado à direita com largura de 10 espaços.

def formata_preco(valor):
    valor_formatado = f"{valor:.2f}"
    return f"{valor_formatado:>10}"

print(formata_preco(55.567))
print()
# 5️⃣ Faça um menu de opções com f-strings e strings multilinha onde o usuário possa escolher:
    # 1 - Converter para maiúsculas
    # 2 - Converter para minúsculas
    # 3 - Contar letras 'e'
# Após o usuário digitar sua frase e escolher a opção, exiba o resultado.

menu = """ Escolha uma opção:\n
1 - Converter para maiúsculas
2 - Converter para minúsculas
3 - Contar letras 'e'
"""

print(menu)

escolha_usuario = input('Digite o número da opção: ')

def formatacao_string(opcao):
    while not opcao.isdigit():
        opcao = input('Opção inválida! Digite um número: ')
    
    opcao = int(opcao)
    frase = input("Digite sua frase: ")

    if opcao == 1:
        return frase.upper()
    elif opcao == 2:
        return frase.lower()
    elif opcao == 3:
        quantidade = frase.lower().count('e')
        return f"Quantidade de letras 'e': {quantidade}"
    else:
        return "Opção inválida."
            
print(formatacao_string(escolha_usuario))