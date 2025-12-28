# reduce - faz a redução de um iterável em um valor unico
# sintaxe - reduce(funcao, iterável, valor_inicial(opcional))
# o valor_opcional serve para garantir que o programa não quebre
# se o iterável estiver vazio
#
from functools import reduce

separator = "-" * 40
products = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]

print("\nReduct Forma Imperativa(Passo a Passo):")
valor = 0
for somar in products:
    valor += somar["preco"]

print(f"Total: {valor:.2f}")

print(separator)

print("\nReduct Forma Funcional:")
valor = reduce(lambda total, produto: total + produto["preco"], products, 0)

print(f"Total: {valor:.2f}")

print(separator)

print("\nReduct Forma Funcional com Função como Argumento:")
def soma_total(total, produto):
    return total + produto["preco"]

valor = reduce(soma_total, products, 0)

print(f"Total: {valor:.2f}")
#
# A sintaxe do reduce:
# Acumulador(Primeiro Argumento) -> Vamos chamar de ACC
#
# Elemento(Segundo Argumento) -> Vamos chamar de Item
#
# Iterável(Terceiro Argumento) -> list, tuple, set, dict, str, etc.
#
# Valor Inicial(Quarto Argumento) -> Ele é opcional, mas é vital
#
# para garantir que o programa não quebre se o iterável estiver vazio.

# FLUXO DO PROGRAMA, COMO FUNCIONA O REDUCE
#
# Vamos imaginar uma lista com 4 elementos:
# numeros = [1, 2, 3, 4]
#
# 1. Pega o primeiro elemento do iterável(ACC) e o Segundo(Elemento)
# 1(ACC) + 2(Elemento) -> 3(ACC)
#
# 2. No segundo passo, ele pega o ACC(3) e o Terceiro(Elemento)
# 3(ACC) + 3(Elemento) -> 6(ACC)
#
# 3. No terceiro passo, ele pega o ACC(6) e o Quarto(Elemento)
# 6(ACC) + 4(Elemento) -> 10(ACC) - (Resultado Final)
#
print(separator)
#
print("\nTestando valor inicial do reduce(Quarto Argumento):")
list_falsy = []
print("Lista Vazia:", list_falsy)
print("Resultado da lista_vazia, pegando o valor inicial:", 
        reduce(soma_total, list_falsy, 0))

print(separator)

print("\nTrabalhando com Strings com o reduce():")
phrase_list = ["O", "Python", "é", "Legal!"]
print("Phrase List:", phrase_list)

function_acc = lambda total, palavra: total + " " + palavra

function_reduce = reduce(function_acc, phrase_list, "")
print(f"Function Reduce: {function_reduce}")
#
print(separator)
#
# -------------------------------------------------------------------------------
# Reduce vs Loops Tradicionais
#
print("\nSUBSTITUINDO REDUCE() POR FUNÇÕES MODERNAS E LEGÍVEIS")
# Em Python moderno, o "reduce" perdeu um pouco de espaço para funções específicas,
# que são mais legíveis e rápidas.
#
# 1. Soma: Em vez de utilizar, reduce(lambda x, y: x + y, iterável). Use sum().
#
# Exemplo:
#
list_numbers = [1, 2, 3, 4, 5]
#
# Maneira Antiga: Imperativa:
# reduce(lambda x, y: x + y, lista_numbers))
#
print("\nSUBSTITUINDO REDUCE() POR SUM()")
print("Total:", sum(list_numbers))
#
# -------------------------------------------------------------------------------
# 2. Maior/Menor: Em vez de utilizar, 
# reduce(lambda x, y: x if x >(<) y else y, iterável). Use max() ou min().
#
# Exemplo:
#
# Maneira Antiga: Imperativa:
# reduce_maior = reduce(lambda x, y: x if x > y else y, lista_numbers)
# reduce_menor = reduce(lambda x, y: x if x < y else y, lista_numbers)
#
print("\nSUBSTITUINDO REDUCE() POR MAX() E MIN()")
print("Maior com a função max():", max(list_numbers))
print("Menor com a função min():", min(list_numbers))
#
# -------------------------------------------------------------------------------
# 3. Concatenar Strings: Em vez de utilizar, 
# reduce(lambda total, palavra: total + " " + palavra). Use "".join().
#
# Exemplo:
#
list_strings = ["O", "Python", "é", "Legal!"]
#
# Maneira Antiga: Imperativa:
# reduce(lambda total, palavra: total + " " + palavra, list_strings)
#
print("\nSUBSTITUINDO REDUCE() POR JOIN()")
print("Concatenando Strings com join():", " ".join(list_strings))
#
# -------------------------------------------------------------------------------
# 4. Tamanho Strings: Em vez de utilizar, 
# reduce(lambda total, palavra: total + len(palavra), iterável). Use len().
#
# exemplo:
#
# Maneira Antiga: Imperativa:
# reduce(lambda total, palavra: total + len(palavra), list_strings, 0)
#
print("\nSUBSTITUINDO REDUCE() POR LEN()")
print("Quantidade de Strings com len():", len(" ".join(list_strings)))
#
# -------------------------------------------------------------------------------
# Mas quando podemos utilizar o reduce(), hoje em dia?
# Quando temos uma lógica de acumulação complexa que não existe pronta
# (ex: multiplicar todos os números, ou fundir um dicionário progressivamente).
#
print(separator)
#
print("\nFUNDIR UM DICIONÁRIO PROGRESSIVAMENTE COM REDUCE()")

configurations = [
    {"tema": "claro", "fonte": 12},
    {"fonte": 14, "cor": "azul"},
    {"log": True}
]

print("Dicionário Original:")
for config in configurations:
    print(f" - {config}")


def merge_configs(dict_acc, dict_next):
    return {**dict_acc, **dict_next}

dict_final = reduce(merge_configs, configurations, {})

print("\nDicionário Final:")
for key, value in dict_final.items():
    print(f" - {key}: {value}")
#
# Quando as keys forem iguais, o reduce() vai sobreescrever o valor, com o 
# valor do dicionário seguinte.
