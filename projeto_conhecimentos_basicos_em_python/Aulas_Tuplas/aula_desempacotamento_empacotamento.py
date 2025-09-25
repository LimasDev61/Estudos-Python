# Introdução ao Desempacotamento de Tuplas
# ........................................................................

# Desempacotamento de tuplas
# ........................................................................

nomes = ("Renan", "Alves", "da", "Silva", "Lima")
nome1, nome2, nome3, nome4, nome5 = nomes
print(f"Olá, {nome1} {nome2} {nome3} {nome4} {nome5}")

# Empacotamento de tuplas
# ........................................................................

nomes = ("Renan", "Alves", "da", "Silva", "Lima")
nomes = list(nomes) # Transformando a tupla em uma lista
nomes[0] = "João" # Modificando o primeiro valor da lista
nomes = tuple(nomes) # Transformando a lista em uma tupla
print(nomes)

# Desempacotamento de tuplas
# ........................................................................

nomes = ("Renan", "Alves", "da", "Silva", "Lima")
nome1, *_ = nomes # Desempacotando a tupla, pegando o primeiro valor. *_ = não queremos pegar o restante
print(f"Olá, {nome1}")

# Utilizando o _ para pegar apenas o segundo valor
nomes = ("Renan", "Alves", "da", "Silva", "Lima")
_, nome2, *_ = nomes
print(f"Olá, {nome2}")

# Pegando o primeiro valor, segundo valor e o restante

nome, * resto = nomes
print(f"Olá, {nome}")
print(f"Olá, {resto}")
