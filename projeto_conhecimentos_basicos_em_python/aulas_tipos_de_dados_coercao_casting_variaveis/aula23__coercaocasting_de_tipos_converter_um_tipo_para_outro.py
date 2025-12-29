# Como Casting, pode ser chamado: 
# Conversão de tipos, coerção,
# Type Convertion, Type Casting, Type Coercion
# é o ato de converter um tipo para o outro
# tipos imutáveis e primitivos:
# int, float, str, bool, complex

# Casting
print(int("10")) # Converte de string para int
print(str(10)) # converte de int para string

# Casting Implicito
int_numero = 10
float_numero = 3.14

resultado = int_numero + float_numero
print(resultado)

# Casting Explicito
pi_numero = 3.14159
int_pi = int(pi_numero)
print(int_pi)

# Type para confirmar o tipo com o casting
print(int('1'), type(int('1')))

# Somar com uma string convertida
print(int('1') + 1)

# Converter para string
print(str(1) + 'b')