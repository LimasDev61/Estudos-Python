# isinstance - é um método que verifica se um objeto pertence a um determinado
# tipo(classe).

lista = ["a", 1, 1.1, True, [0, 1, 2], (0, 1, 2), {1, 2}, {"nome": "Renan"}, \
        None]

for item in lista:
    print(f"{item} - {isinstance(item, str)}")

print("\n")
for item in lista:
    print(f"{item} - {isinstance(item, list)}")

print("\n")
for item in lista:
    if isinstance(item, set):
        print("SET:")
        item.add(3)
        print(item, isinstance(item, set))

    # Não consigo mudar o item, pois ele é uma string, é imutável,
    # ou seja, ele nao pode ser alterado, apenas modificado nela mesma.
    # Modelo com Erro - não acontece nada.
    elif isinstance(item, str):
        print("STR:")
        item.upper()
        print("Modelo com erro:",item, isinstance(item, set))

    # Modelo Correto
    elif isinstance(item, str):
        print("Modelo correto:", item.upper(), isinstance(item, str)) # Alterado para maiusculo

    elif isinstance(item, (int, float)):
        print("INT ou FLOAT:")
        print(item, item * 2)

    else:
        print("Outro tipo:")
        print(item)