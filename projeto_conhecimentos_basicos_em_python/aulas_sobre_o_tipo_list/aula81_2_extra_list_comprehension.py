# List Comprehension - Comprenhensão de Listas
# Uma forma de criar listas com base em outras listas
# Sintaxe: [expressão for item in list]
# Sintaxe: [expressão for item in list if condicional]
# Sintaxe: [expressão for item in list1 if condicional1 if condicional2]
# Sintaxe: [expressão for item in list1 if condicional1 if condicional2 if condicional3]

# Exemplos:

# Criando uma lista com os quadrados dos números de 1 a 10
quadrados = [x**2 for x in range(1, 11)]
print(quadrados)

# Criando uma lista com os quadrados dos números pares de 1 a 10
quadrados_pares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(quadrados_pares)

# Criando uma lista com os quadrados dos números impares de 1 a 10
quadrados_impares = [x**2 for x in range(1, 11) if x % 2 == 1]
print(quadrados_impares)

# Criando uma lista com os quadrados dos números pares e impares de 1 a 10
quadrados_pares_impares = [x**2 for x in range(1, 11) if x % 2 == 0 if x % 2 == 1]
print(quadrados_pares_impares)

# Criando uma lista com os quadrados dos números pares e impares de 1 a 10
quadrados_pares_impares = [x**2 for x in range(1, 11) if x % 2 == 0 if x % 2 == 1]
print(quadrados_pares_impares)