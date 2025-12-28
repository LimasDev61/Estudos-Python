# Considerando duas listas de inteiros ou floats (lista_a e lista_b),
# Some os valores nas listas retornando uma nova lista com os valores somados:
# Se uma lista for maior que a outra, a soma apenas vai considerar o tamanho da menor.
# Exemplo:
# lista_a     -> [1, 2, 3, 4, 5, 6, 7]
# lista_b     -> [1, 2, 3, 4]
# retorno -> [2, 4, 6, 8]
from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def somar_listas(lista_a, lista_b):
    def wrapper_soma():
        return [x + y for x, y in zip(lista_a, lista_b)]
    return wrapper_soma


soma = somar_listas(lista_a, lista_b)
print("Soma entre Lista A e B:", soma())

# Teste da fábrica de funções
soma2 = somar_listas(lista_a, lista_c)
print("Soma entre Lista A e C:", soma2())

print()
# Com zip_longest: pega os valores restantes da lista
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print("Soma entre Lista A e B com zip_longest:", lista_soma)