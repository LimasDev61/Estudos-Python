# Tipo tupla - Uma lista imutável

nomes = ("Renan", "Alves", "da", "Silva", "Lima") # Com parentêses
print(nomes)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 # Sem parentêses - empacotamento
print(numeros)
print(numeros[-1]) # Pegando o ultimo valor

# Converter uma tupla em uma lista
# Não faz muito sentido fazer essa conversão, porque
# se você precisar alterar algum valor, crie uma lista
alterar = list(nomes)
alterar[0] = "João"
alterar = tuple(alterar)
print(alterar)