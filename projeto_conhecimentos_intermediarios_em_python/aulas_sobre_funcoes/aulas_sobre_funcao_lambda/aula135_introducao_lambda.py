# Função lambda em Python
# A função lambda é  como qualquer outra em Python.
# Porém, são funções anônimas(sem nome), que contêm apenas uma linha.
# Ou seja, tudo deve ser contido em uma única expressão.
# Sintaxe: lambda argumentos: expressão

# Exemplo 1: Função tradicional - alta ordem
lista_numerica = [4, 32, 1, 5, 7, 9, 10, 3, 0, 6, 8, 2, 11]
print("Lista Original:", lista_numerica)
nova_lista_numerica = sorted(lista_numerica) # cópia rasa
print("Nova Lista:", nova_lista_numerica)

lista_numerica.sort() # cópia profunda
print("Lista Original, Alterada:", lista_numerica) # a lista_numerica original é alterada # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 32]
lista_numerica.sort(reverse=True)
print("Lista Original, reverse:", lista_numerica) # Saída: [32, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("\n")

lista = [
    {"nome": "Luiz", "sobrenome": "Otávio"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Helena", "sobrenome": "Souza"},
    {"nome": "João", "sobrenome": "Miranda"},
    {"nome": "Renan", "sobrenome": "Lima"},
]

print("Lista Original:")
for item in lista:
    print(item)

print("\n")
# Exemplo 2: função tradicional
print("Lista Ordenada:")
def orden(item):
    return item['nome']

lista.sort(key=orden)
for item in lista:
    print(item)

print("\n")

# Exemplo 3: função lambda
print("Lista Ordenada, lambda:") 
lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)

print("\n")

# Exemplo 3.1 - função lambda com sorted
print("Lista Ordenada, lambda com sorted, pelo sobrenome:")
lista.sort(key=lambda item: item['sobrenome'])
for item in lista:
    print(item)