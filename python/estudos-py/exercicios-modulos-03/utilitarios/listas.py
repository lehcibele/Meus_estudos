# 4️⃣ Exercício — Pacote de Utilitários
# Crie um pacote chamado utilitarios com:
    # strings.py: função que inverte uma string;
    # listas.py: função que remove duplicatas de uma lista.
# Teste essas funções em outro arquivo.

def removeDuplicatas(lista):
    dicionarios_elemento = {}
    lista_sem_duplicatas = []
    for item in lista:
        if item not in dicionarios_elemento:
            dicionarios_elemento[item] = True
            lista_sem_duplicatas.append(item)
    return lista_sem_duplicatas    
    