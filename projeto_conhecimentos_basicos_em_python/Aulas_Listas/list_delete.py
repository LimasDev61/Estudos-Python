# # Métodos e Instruções - Para Remover
# ..................................................
# remove - Remove um item da lista por valor
# pop - Remove um item da lista por indice, retorna o item removido
# del - Remove um item da lista por indice ou posição
# clear - Limpa a lista
# ..................................................
# Exemplos:
# ..................................................

# Removendo por Remove e Seu Valor - numérico ou string
print("\nRemovendo por Remove:")
lista_nomes = ['Geek', 'University', 'Python', 'Linguagem', 'Faculdade']
lista_nomes.remove("Linguagem")
print(f"lista_nomes = {lista_nomes}")

# Removendo por Pop, retorna o item removido
print("\nRemovendo por Pop:")
lista_nomes2 = ['Geek', 'University', 'Python', 'Linguagem', 'Faculdade']
item_removido = lista_nomes2.pop(2)
print(f"item_removido = {item_removido}")
print(f"lista_nomes = {lista_nomes2}")

# Posso usar o pop para acrescentar o item removido em uma nova lista
print("\nAcrescentando o item removido de uma lista para a outra:")
numeros = [1, 2, 3, 4, 5]
numeros2 = []
numeros2.append(numeros.pop(2))
print(f"numeros = {numeros}")
print(f"numeros2 = {numeros2}")

# Removendo por Del
print("\nRemovendo por Del:")
lista_nomes3 = ['Geek', 'University', 'Python', 'Programação', 'Faculdade']
del lista_nomes3[2]
print(f"lista_nomes = {lista_nomes3}")

# Del também aceita slices
print("\nRemovendo por Del com Slice:")
lista_nomes4 = ['Geek', 'University', 'Python', 'Programação', 'Faculdade']
del lista_nomes4[1:4]
print(f"lista_nomes = {lista_nomes4}")

# Clear - Limpa a lista
print("\nClear - Limpa a lista:")
lista_nomes5 = ['Geek', 'University', 'Python', 'Program', 'Faculdade']
lista_nomes5.clear()
print(f"lista_nomes = {lista_nomes5}")