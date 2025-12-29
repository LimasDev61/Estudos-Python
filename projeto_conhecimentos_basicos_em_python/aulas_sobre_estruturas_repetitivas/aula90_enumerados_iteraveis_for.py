# Enumerate
# enumerate -> Enumera itens de uma estrutura iteração

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Jeito Antigo
for indice in range(len(lista)):
    print(indice, lista[indice])

print()
# Jeito Novo
for indice, letra in enumerate(lista):
    print(indice, letra)

print()
# Definindo um indice - inicial (enumerate(valor, start=100))
for indice, letra in enumerate(lista, 1):
    print(indice, letra)

print()
# Desempacotamento, tupla
for item in enumerate(lista):
    indice, nome = item
    print(item)


# Quando eu faço um desempacotamento do enumerate, ele vira uma tupla.

# Exemplo prático:

print()
print("Exemplo de uso para transformar uma lista em uma lista enumerada como tupla:")
lista_nomes = ['Renan', 'Ana', 'Maria', 'João']

lista_enumerada = list(enumerate(lista_nomes)) # <- Jeito Resumido.
print(lista_enumerada)

# Ou:
lista_enumerada2 = enumerate(lista_nomes)
print(list(lista_enumerada2))

# Ou
for item in enumerate(lista_nomes):
    print(item) # <- sai um em baixo do outro.
