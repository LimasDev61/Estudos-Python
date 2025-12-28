# List Comprehension em Python
# É uma forma rápida para criar listas a partir de outras listas ou iteráveis.

# Sintaxe Forma Tradicional
# Elevar o quadrado todos os elementos de uma lista

quadrados = []
for x in range(6):
    quadrados.append(x ** 2)

print(quadrados)

# List Comprehension

# Elevar o quadrado todos os elementos de uma lista
# Forma 1 - Sintaxe = [expressão for item in list]
quadrados = [x ** 2 for x in range(6)]
print(quadrados)

# Pegar os numeros pares de uma lista até o 10
# Forma 2 - Sintaxe Condicional = [expressão for item in list if condicional]
numeros_pares = [num for num in range(11) if num % 2 == 0]
print(numeros_pares)

# Diferenciar par de impa com um ternario
# Forma 3 - Sintaxe Condicional = 
# [expressão if condicional else expressão for item in list]
numeros_pares_impares = ['par' if num % 2 == 0 else 'impar' for num in range(6)]
print(numeros_pares_impares)

# Achatar uma matrix de 3x3 em uma unica lista
# Forma 4 - Sintaxe Matriz = [expressão for item in list for item in list]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista = [num for item in matrix for num in item]
print(lista)

# Achatar uma matrix 3x3 em uma tupla
# Forma 5 - Sintaxe Matriz = [expressão for item in list for item in list]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tupla = tuple(num for item in matrix for num in item)
print(tupla)


tupla = (2, 3)

total = [x ** 2 for x in tupla]
print(total)

listas = []
for x in tupla:
    listas.append(x ** 2)

tuplas = tuple(listas)    
print(tuplas)

# Pegar o nome de 2 em 2 caracteres
strings = "Renan Lima"
numeros_de_letras = 2
strings_modificada = [strings[indice:indice + numeros_de_letras] \
                        for indice in range(0, len(strings), numeros_de_letras)]

print(strings_modificada)

# Pegar o quadrado de todos os numeros de 0 a 9
numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)