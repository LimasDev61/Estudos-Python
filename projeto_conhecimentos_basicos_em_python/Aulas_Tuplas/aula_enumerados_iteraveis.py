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


# obs: quando coloco o enumarate em uma variável, ele cria um objeto de uso limitado
# ou seja, ele consome a memória.
# outra coisa, um enumarate dentro de yma variável, é uma tupla.