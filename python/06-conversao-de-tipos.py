# Conversão de tipos: chamados também de coerção, type convertion, typecasting, coercion.
# É o ato de converter um tipo em outro:
# Tipos imutáveis e primitivos: str, int, float, bool

print(int('1'), type(int('1')))
print(float('1.2') + 1)
print(str(11) + 'b')

# string vázia é considerada False, mas se tiver um espaço é considerada True
print(bool(' '))