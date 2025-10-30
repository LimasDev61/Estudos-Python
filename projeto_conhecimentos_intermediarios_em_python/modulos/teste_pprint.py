import pprint

produtos = [
    {'zona': 'x', 'preco': 20},
    {'aleluia': 'a', 'preco': 10},
    {'sistema': 'c', 'preco': 30},
]

novos_produtos = [{**produto, "preco": produto["preco"] * 1.05} \
                if produto["preco"] > 20 else {**produto} \
                for produto in produtos]


pprint.pprint(novos_produtos, sort_dicts=True, width=40)

numeros = [n for n in range(5) if n != 3]

pprint.pprint(numeros)


# Sort_dicts=True, mostra as chaves de dicionários em ordem alfabetica