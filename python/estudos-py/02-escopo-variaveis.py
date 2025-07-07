# Crie uma função que declare uma variável local e imprima seu valor.
def saudacao():
    mensagem = "Olá, Mundo!"
    print(mensagem)
saudacao()

# Crie uma variável global e acesse ela dentro de uma função (sem modificar)
valor = 10
def exibir():
    print(valor)
exibir()

#Crie uma variável global e uma função que incremente seu valor usando global.
contador = 0
def soma():
    global contador
    contador += 1
    print(contador)
soma()

# Refatore o exercício 3 para resolver sem usar global, apenas com argumentos e return
contador = 0
def soma(cont):
    cont += 1
    return cont
print(soma(contador))
