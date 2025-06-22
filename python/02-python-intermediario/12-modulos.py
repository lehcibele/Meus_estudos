"""
    Formas de importa os módulos:
        import sys # sai do programa no terminal
        from sys import exit, platform # importa apenas esses dois do modulo
        import sys as s 
        from sys import exit as ex
        from sys import platform as pf
        from sys import*
"""

"""
    O primeiro módulo executado chama-se __main__
    Você pode importar outro módulo inteiro ou parte do módulo.
    O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
    Ele não reconhece pastas e módulos acima do __main__ 
    por padrão o python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
"""

import importlib # para recarregar o módulo
import modulo_m_12 
from modulo_m_12 import soma, variavel_modulo # importa a função soma e a variavel

print('Este módulo se chama', __name__)
print(modulo_m_12.variavel_modulo)
print(variavel_modulo)
print(modulo_m_12.soma(5, 5))
print(soma(2, 3))
for i in range(10):
    importlib.reload(modulo_m_12)
    print(i)
    
print('Fim')