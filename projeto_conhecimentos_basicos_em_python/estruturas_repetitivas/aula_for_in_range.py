# For In Range() é uma estrutura de repetição que percorre uma sequência numérica gerada pela função range(start, stop, step)

# Exemplo com range()

numeros = range(10) # Quando se passa apenas um parâmetro, ele é o stop e o start é 0

for numero in numeros:
    print(numero, end=' ')


numeros_pula_de_2_em_2 = range(0, 100, 2) # start, stop, step

for numero in numeros_pula_de_2_em_2:
    print(numero, end=' ')

# Range negativo
numeros_negativos = range(10, -100, -20)
for numero in numeros_negativos:
    print(numero, end=' ')

print("\n")

# Decremento
# 100, 99, 98, 97, ..., 0
for numero in range(100, -1, -1):
    print(numero)