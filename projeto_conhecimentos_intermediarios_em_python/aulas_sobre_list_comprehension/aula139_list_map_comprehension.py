# Mapeamento de dados com list comprehension
# O mapeamento serve para modificar os dados de uma lista

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [{**produto, "preco": produto["preco"] * 1.05} \
                if produto["preco"] > 20 else {**produto} \
                for produto in produtos]

print(*novos_produtos, sep='\n')

# Filtrar numeros maiores que 10 de uma lista - map
numeros = [5, 12, 25, 10, 2, 3, 100]

numeros_maiores = [num for num in numeros if num > 10]
print(numeros_maiores)