# Iterables e Iterators em Python
# Iterables: objetos que podem ser percorridos, como listas, tuplas, dicionários 
# e conjuntos.
# Iterators: a função iter() cria um iterator a partir de um iterable.
# Os iterators podem ser usados para percorrer os elementos de um iterable,
# mas eles também podem ser usados para criar novos iterables.

# Exemplo de Iterable
iterable = [1, 2, 3, 4, 5]
iterator = iter(iterable)

print(next(iterator))  # Saída: 1
print(next(iterator))  # Saída: 2
print(next(iterator))  # Saída: 3

# Função next para iterar sobre um iterable de um em um.

# Podendo também utilizar ele assim:
iterable_1 = [1, 2, 3, 4, 5]
iterator_1 = iterable_1.__iter__()
print(next(iterator_1))
print(next(iterator_1))
print(next(iterator_1))

# Exemplo de Iterator
iterator_2 = iter([1, 2, 3, 4, 5])

print(next(iterator_2))  # Saída: 1
print(next(iterator_2))  # Saída: 2
print(next(iterator_2))  # Saída: 3
