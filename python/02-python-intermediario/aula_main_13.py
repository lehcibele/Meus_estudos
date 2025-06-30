from sys import path

# importando a pasta package
# import aula13_package.modulo_13 # importa toda a pasta
# from aula13_package.modulo_13 import soma_do_modulo

# from aula13_package import modulo_13 # importa o arquivo
# from aula13_package.modulo_13 import *  # importa tudo do arquivo, mas como tem o all no outro modulo só importa o que tem no all
import aula13_package

# print(soma_do_modulo(1, 2))
# print(soma_do_modulo(5, 3))

print(aula13_package.soma_do_modulo(2, 3))