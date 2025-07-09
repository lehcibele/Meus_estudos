# 1️⃣ Usando range():
# Crie uma função que:
    # Recebe um número n.
    # Exibe todos os números de 1 até n.
    # Exibe a soma de todos esses números.

def exibir_numeros(n):
    soma = 0
    for numero in range(1, n+1):
        soma += numero
        print(numero)
    print(soma)

exibir_numeros(10)

# 2️⃣ Usando enumerate():
# Crie uma função que:
    # Recebe uma lista de compras.
    # Mostra os itens com numeração iniciando em 1.

def lista_compras(lista):
    for indice, item in enumerate(lista, start=1):
        print(f"{indice}. {item}")

lista_de_compras = ['Feijão', 'Arroz', 'Macarrão', 'Leite', 'café', 'Suco', 'Banana', 'Pipoca']
lista_compras(lista_de_compras)

# 3️⃣ Usando zip():
# Crie uma função que:
    # Recebe duas listas: nomes e notas.
    # Mostra o nome de cada aluno com sua nota.

def exibir_nomes(alunos, notas):
    for nome, nota in zip(alunos, notas):
        print(f"{nome} {nota}")

nomes_de_alunos = ['Lucas', 'Levi', 'Paulo', 'Ana']
notas_de_alunos = [10, 7, 5, 4]
exibir_nomes(nomes_de_alunos, notas_de_alunos)

# 4️⃣ Desafio Extra com range():
# Crie um gerador de tabuada:
    # Recebe um número.
    # Exibe a tabuada de 1 a 10 desse número.

def tabuada(numero):
    for num in range(1, 11):
        print(f"{numero} x {num} = {numero * num}")
    
tabuada(5)

# 5️⃣ Desafio Extra com enumerate() e zip():
# Receba duas listas:
    # Produtos e Preços.
    # Exiba um relatório numerado:
    # 1 - Produto: Arroz | Preço: R$ 5.00

def exibirRelatorio(produtos, precos):
    produto_preco = list(zip(produtos, precos))
    for indice, (produto, preco) in enumerate(produto_preco, start=1):
        print(f"{indice} - Produto: {produto} | Preço: {preco:.2f}")

lista_de_produtos =  ['Feijão', 'Arroz', 'Macarrão', 'Leite', 'café']
lista_de_precos = [10.98, 6.00, 3.50, 6.75, 13.45]
exibirRelatorio(lista_de_produtos, lista_de_precos)