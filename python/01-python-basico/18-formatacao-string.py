"""
Formatação de Strings 
s -> string
d -> inteiro 
f -> float
.<número de digitos>f -> número de dígitos após a vírgula
x ou X -> hexadecimal
(Caractere) (<>^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0 > -100:.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:1>10}')   # 1111111ABC coloca 1 a esquerda até completar 10 caracteres
print(f'{variavel:2<10}')   # 2222222ABC coloca 2 a direita até completar 10 caracteres
