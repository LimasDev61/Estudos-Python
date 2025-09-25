# Métodos - Para Adicionar
# ..................................................
# append - Adiciona um item ao final da lista
# insert - Adiciona um item em uma posição específica da lista
# extend - Adiciona uma lista em outra
# operador + - Adiciona uma lista em outra, criando uma nova lista, polimorfismo
# ..................................................
# Exemplos:
# ..................................................

# Adicionando por Append
print("\nAdicionando por Append:")
lista_nomes = ['Geek', 'University', 'Python', 'Programação', 'Faculdade']
lista_nomes.append("Renan")
print(f"lista_nomes = {lista_nomes}")

# O Append pode ser usado para adicionar um item em uma lista, mas também pode ser usado para adicionar uma lista em outra
print("\nAdicionando por Append, uma lista a outra:")
lista_numeros_append1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros_append2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_numeros_append1.append(lista_numeros_append2)
print(f"lista_numeros_append1 = {lista_numeros_append1}")

# Adicionando por Insert
print("\nAdicionando por Insert:")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros.insert(2, 20)
print(f"lista_numeros = {lista_numeros}")

# Adicionando por Extend
print("\nAdicionando por Extend:")
lista_numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_numeros1.extend(lista_numeros2)
print(f"lista_numeros1 = {lista_numeros1}")

# Adicionando por Operador +
print("\nAdicionando por Operador +:")
lista_numeros3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros4 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_numeros5 = lista_numeros3 + lista_numeros4
print(f"lista_numeros5(Combinação das duas listas, criando uma nova) = {lista_numeros5}")

# Também temos como adiciona diretamente pelo indice
print("\nAdicionando diretamente pelo indice:")
lista_numeros6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros6[2] = 20
print(f"lista_numeros6 = {lista_numeros6}")