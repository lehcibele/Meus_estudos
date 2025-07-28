# 1️⃣ Crie uma tupla com 5 números e:
#   Mostre o maior, menor, soma e média dos valores.

tupla_numeros = (25, 12, 8, 54, -9)

maior = max(tupla_numeros)
menor = min(tupla_numeros)
soma = sum(tupla_numeros)
media = soma / len(tupla_numeros)

print(f"O maior valor é {maior}, o menor valor é {menor}, a soma dos valores é {soma} e a média é {media:.2f}")

# 2️⃣ Faça uma função que recebe uma tupla e retorna quantas vezes o número 0 aparece.

def numero_0_aparece(args):
    valor = 0
    total_zeros = args.count(valor)
    return total_zeros

entrada = input("Digite os valores: ")
valores = tuple(map(int, entrada.split())) # converte a entrada em uma tupla de inteiros
total_0 = numero_0_aparece(valores)
print(total_0)

# 3️⃣ Desempacote a tupla dados = ('Letícia', 24, 'Python') em três variáveis e imprima uma frase com eles.
dados = ('Letícia', 25, 'Python')
nome, idade, linguagem = dados
print(f"Meu nome é {nome}, e tenho {idade} anos e estou estudando a linguagem de programação {linguagem}")

# 4️⃣ Crie uma tupla com 10 nomes. Peça ao usuário para digitar um nome e diga se está ou não na tupla.
tupla_animais = ("gato", "leão", "cachorro", "girafa", "elefante", "rato", "tubarão", "cavalo", "zebra", "onça")

nome_animal = input("Digite um nome de um animal: ").lower()

acertou = False

if nome_animal in tupla_animais:
    print("Parábens você acertou!!")
else:
    print("Você errou :(")

# 5️⃣ Crie uma tupla que simule um cardápio de lanchonete (item, preço). Depois mostre todos os itens formatados:

cardapio = ( ("Hamburguer", 10.00), ("Batata Frita", 5.00), ("Pizza", 40.00) )

print("🍔 Cardápio: ")

for index, tipo_lanche in enumerate(cardapio):
    lanche, valor = tipo_lanche
    print(f"{index + 1} - {lanche} .......... R${valor}")