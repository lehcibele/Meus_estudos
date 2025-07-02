"""
    Criando arquivos com python
    Usamos a função open para abrir um arquivo em python (ele pode ou não existir).
    Modos:
        r -> Leitura
        w -> Escrita
        x -> Criação
        a -> Escreve ao final
        b -> Binário
        t -> Modo texto 
        + -> leitura e escrita
    
    Context manager:
        with -> abre e fecha

    Métodos úteis:
        write -> escrever
        read -> ler
        writelines -> escreve várias linhas
        seek -> move o cursor
        readline -> ler linha
        readliines -> ler linhas

    Módulo os:
        os.remove ou unlink -> apaga o arquivo
        os.rename -> troca o nome ou move arquivo

    Módulo JSON:
        json.dump -> Gera um arquivo json
        json.load -> 

"""
caminho_arquivo = 'C:\\Users\\letic\\Documents\\MeusProjetos\\Meus_estudos\\python\\02-python-intermediario\\'
caminho_arquivo += '17-aula.txt'

# Cria o arquivo ('w') 
# arquivo = open(caminho_arquivo, 'w')

# # Fecha o arquivo
# arquivo.close()

# Cria o arquivo e já fecha igual o código acima, o + é para ser escrita + leitura
with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.readline())

# abre ler o arquivo 'r' e fecha o arquivo
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())