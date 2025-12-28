# Assim como a comprehension de listas, podemos criar compreensões de sets.
# A sintaxe utiliza chaves em vez de colchetes.
# Sintaxe: {expressão for item in list}

# Exemplo 1 - Mapeamento de dados
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = {num: num ** 2 for num in numeros}
print(quadrados)

# Exemplo 2 - Diminuir nomes e manter e tirar redundancias
nomes = ["Renan", "Amora", "amora", "renan", "Stephane"]
nomes_unicos = {nome.lower() for nome in nomes}
print(nomes_unicos)

# Exemplo 2 - Criar um set com apenas multiplos de três
multiplos_de_tres = {num for num in range(1, 21) if num % 3 == 0}
print(multiplos_de_tres)


# Parte da Aula

s1 = {i for i in range(10)} # apenas exemplo
print(s1)

# melhor passar como exemplo: print(set(range(10)))