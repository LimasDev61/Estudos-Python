# map - para mapear dados sem o partial
def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

separador = "-" * 40

print("\nmap(), mapeando dados sem o partial:")
product = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]

def aumentar_porcentagem(value, percentage):
    return round(value * percentage, 2)

new_product_1 = [
    {**product, "preco": aumentar_porcentagem(product["preco"], 1.05)}
    for product in product
]

print_iter(new_product_1)

print(separador)

# partial - para mapear dados com o partial + map
from functools import partial

# High Order Function - Ela está recebendo uma função como parâmetro - aumentar_porcentagem
def increase_price_product(product, percentage):
    return {**product, "preco": aumentar_porcentagem(product["preco"], percentage)}

increase_ten_percent = partial(increase_price_product, percentage=1.10)

new_product_2 = map(increase_ten_percent, product)

print("\nnew_product_2, foi consumido:")
print_iter(new_product_2)

# GeneratorType e Esgotamento de Iterators
from types import GeneratorType

print(f"\nnew_product_2. É um GeneratorType? {isinstance(new_product_2, GeneratorType)}, ele é da classe: {type(new_product_2).__name__}")
print(f"new_product_2. É um Iterador? {hasattr(new_product_2, '__next__')}")

print("\nEsgostamento do Iterador new_product_2:")
print(f"Segunda chamada, esgotado: {list(new_product_2)}")

print(separador)

# Testando um iterador com o GeneratorType
print("\nTestando um iterador com o GeneratorType")
generator = (x * 2 for x in [1, 2])

print(f"generator. É um GeneratorType? {isinstance(generator, GeneratorType)}")
print(f"generator. É um Iterador? {hasattr(generator, '__next__')}")

print("\nEsgostamento do Iterador generator:")
print(f"Primeira chamada, resultado do generator: {list(generator)}")
print(f"Segunda chamada, esgotado: {list(generator)}")

# Caso eu precise que o iterador seja reutilizavel, basta eu transformar ele em uma 
# lista ou tupla: new_product_2 = list(map(increase_ten_percent, product)).

# Obs: O partial serve para criar funções com parâmetros fixos(congela o valor do 
# segundo parâmetro). O partial, permite que o map receba dois parâmetros
# (através de uma função partial), em vez de um parâmetro que é seu padrão.