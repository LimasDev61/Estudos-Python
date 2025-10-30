# Funciona de forma semelhante a laços for aninhados tradicioais.
# O primeiro for é o laço mais externo, e o segundo for é o laço mais interno.

#sintaxe dos laços for aninhados
# [expressão for item1 in list1 for item2 in list2]

# Uso comum do laço aninhado
import pprint
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposta = [linha for linha in matriz for linha in linha]
pprint.pprint(transposta)

print("\n")

# Produto Cartesiano
cores = ["red", "blue"]
tamanhos = ["P", "M", "G"]

combinacoes = [(cor, tamanho) for cor in cores for tamanho in tamanhos]
pprint.pprint(combinacoes)

# Filtrar numeros pares em uma matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numeros_pares = [num for linha in matriz for num in linha if num % 2 == 0]
pprint.pprint(numeros_pares)

lista = [(x, y) for x in range(5) for y in range(5)]
pprint.pprint(lista)