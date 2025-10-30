# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    "nome": "Renan",
    "sobrenome": "Lima",
    "idade": 33,
    "altura": 1.69,
    "enderecos": [
        {"rua": 16, "setor": "Oeste", "número": 123},
        {"rua": 25, "setor": "Sul", "número": 321},
    ]
}

print(pessoa.get("nome"), end=" ")  # Renan
print(pessoa.get("sobrenome"))  # Lima

print()

for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")  # print(chave = chave, pessoa[chave] = valor)
