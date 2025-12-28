# filter é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

separador = "-" * 40
print("\nLista Original:")
product = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]

print_iter(product)
print(separador)
print("Filtrando maiores preços com list comprehension(Recomendado):")
new_product_max = [
    products for products in product if products["preco"] > 20
]

print_iter(new_product_max)

print(separador)

print("Filtrando maiores preços de forma Imperativa(Passo a Passo):")

def filter_products(products):
    new_products = []
    for product in products:
        if product["preco"] > 20:
            new_products.append(product)
    return new_products

print_iter(filter_products(product))

print(separador)

print("Filtrando maiores preços com filter(), Funcional:")
new_product_max = filter(lambda product: product["preco"] > 20, product)

print_iter(new_product_max)

print(separador)

# Uma caracteristica importante de filter(), é que se passarmos 
# None no lugar da função, ele remove tudo que for False(Falsy values).
print("Removendo Falsy values com filter():")
dados_list = [0, "Ana", "", False, "Carlos", None, 25, True]

print("Original Dirty List:", dados_list)

clear = list(filter(None, dados_list))
print("\nClear List:", clear)

