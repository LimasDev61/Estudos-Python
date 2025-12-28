# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

print("Minhas Listas:")
city = ["Salvador", "Ubatuba", "Belo Horizonte"]
state = ["BA", "SP", "MG", "RJ"]

print(city)
print(state)

print()

print("\n")

print("Primeira lógica, utilizando o zip e zip_longest:")
def zipper(city, state):
    resultado = []
    for city, state in zip(city, state):
        resultado.append((city, state))
    return resultado

def longest_zipper(city, state):
    resultado = []
    for city, state in zip_longest(city, state, fillvalue="Sem Cidade"):
        resultado.append((city, state))
    return resultado

resultado = zipper(city, state)
texto = str(resultado)
texto = texto.replace("'", '"')
texto_formatado = texto.replace("), ", "),\n ")
print(texto_formatado)

print("\n")

resultado = longest_zipper(city, state)
texto = str(resultado)
texto = texto.replace("'", '"')
texto_formatado = texto.replace("), ", "),\n ")
print(texto_formatado)

print("\n")

# Segunda lógica, utilizando o mesmo caso, porém utilizando len.
# Muito mais complexo...
print("Segunda lógica, utilizando o mesmo caso, porém utilizando len:")
def zipper_len(city, state):
    menor = min(len(city), len(state))
    return [(city[i], state[i]) for i in range(menor)]

resultado = zipper_len(city, state)
texto = str(resultado)
texto = texto.replace("'", '"')
texto_formatado = texto.replace("), ", "),\n ")
print(texto_formatado)

print("\n")
def zipper_longest_len(city, state, fill_city = "Sem Cidade", fill_state = "Sem Estado"):
    maior_tamanho = max(len(city), len(state))
    return [(
        city[i] if i < len(city) else fill_city,
        state[i] if i < len(state) else fill_state
    )
    for i in range(maior_tamanho)
    ]

resultado = zipper_longest_len(city, state)
texto = str(resultado)
texto = texto.replace("'", '"')
texto_formatado = texto.replace("), ", "),\n ")
print(texto_formatado)

# Maneira simples
print("\n")
print("Maneira simples com zip e zip_longest:")
lista_unida_zip = zip(city, state)
print(list(lista_unida_zip))

print("\n")

lista_unida_zip_longest = zip_longest(city, state, fillvalue="Sem Cidade")
print(list(lista_unida_zip_longest))