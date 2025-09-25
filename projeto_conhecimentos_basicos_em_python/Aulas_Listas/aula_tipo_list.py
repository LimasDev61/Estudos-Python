# Listas em Python
# Tipo List -> Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - indexes e slices
# Muito semelhante ao array
# Métodos úteis para listas: append, insert, pop, del, clear, extend, +

# Criando uma lista - Function List
# lista_metodo = list("tudo", "bem")

# Criando uma lista de forma comum, verificando com type o tipo list:
lista_vazia = []
lista_str = ['Geek', 'University']
print(type(lista_str))

# Listas aceitam Differentes Tipos
lista_variada = [1, 'Geek', 3.14, True, []]
print(lista_variada)

# Acessando itens pelo indices
print(lista_str[0])

# Verificando o valor do elemento na lista
print(lista_variada[3], type(lista_variada[3]))

# Também posso converter os valores para upercase e lowercase
print(lista_str[0].upper(), lista_str[1].lower())

# Posso acessar os indices por negativos
print(lista_str[-1]) # acessa o ultimo item da lista - university
print(lista_str[-2]) # acessa o penultimo item da lista - Geek