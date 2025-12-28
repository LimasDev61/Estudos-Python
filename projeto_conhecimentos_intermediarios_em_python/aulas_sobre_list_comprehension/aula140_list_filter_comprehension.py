import pprint

# A condição de filtragem(if) é colocada após a cláusula for.
# e ela decide quais elementos o laço deve processar.

# Sintaxe básica
# [expressão for item in list if condicional]

# Exemplo sintaxe básica
numeros = [5, 12, 25, 10, 2, 3, 100]

# Exemplo sintaxe básica para filtrar maiores que 10
numeros_maiores = [num for num in numeros if num > 10]
print(numeros_maiores)

# Exemplo sintaxe básica para filtrar pares
numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_maiores)

# Filtro dicionário
usuarios = [
    {"nome": "Ana", "status": "ativo"},
    {"nome": "João", "status": "inativo"},
    {"nome": "Maria", "status": "inativo"},
    {"nome": "Pedro", "status": "ativo"},
]


print("\n")
filtro_ativos = [user for user in usuarios if user["status"] == "ativo"]
print("Usuário, Ativo:")
for user in filtro_ativos:
    print(user)

print("\n")

# Combinação de Filtro e Mapeamento

numeros = [2, 4, 5, 6, 7, 8, 9, 10]

elevar = [num ** 2 for num in numeros if num % 2 == 0]
print(elevar)

# Mapeamento de dados com list comprehension
# O mapeamento serve para modificar os dados de uma lista

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# Nunca faça isso pela complexibilidade do código.
novos_produtos = [{**produto, "preco": produto["preco"] * 1.05} \
                if produto["preco"] > 20 else {**produto} \
                for produto in produtos if produto["preco"] >= 20 and produto["preco"] * 1.5 > 30]


pprint.pprint(novos_produtos, sort_dicts=False, width=40)

# Filtro com multiplas condições:

numeros = [2, 4, 5, 6, 7, 8, 9, 10]

elevar = [num ** 2 for num in numeros if num % 3 == 0 and num > 5]
print(elevar)
