# Essas três funções: Combinations, Permutations e Product, fazem parte do modulo itertools
# Elas funcionam como "Canivete Suiço" da análise combinatória em Python. Elas servem para
# criar grupos e sequências a parti de uma lista de itens.

# Resumo Comparativo: Módulo itertools (Arranjos)
# Conjunto de Entrada: C = ['A', 'B'] | Tamanho do Arranjo: r=2
# ------------------------------------|--------------------------------------------------|------------------|-------------------
# Funções                             | Resultados (TODOS os resultados possíveis)         | A Ordem Importa? | Repete Elementos?
# ------------------------------------|--------------------------------------------------|------------------|-------------------
# product(C, repeat=2)                | (A, A), (A, B), (B, A), (B, B)                   | Sim              | Sim
# permutations(C, r=2)                | (A, B), (B, A)                                   | Sim              | Não
# combinations(C, r=2)                | (A, B)                                           | Não              | Não
# combinations_with_replacement(C, r=2) | (A, A), (A, B), (B, B)                           | Não              | Sim

# Product: Cria todos os arranjos de tamanho r da lista C, repetindo os elementos, alterando a ordem.
# Permutations: Cria todas as permutações de tamanho r da lista C, não repete os elementos, altera a ordem.
# Combinations: Cria todas as combinações de tamanho r da lista C, não repete os elementos, a ordem não importa.
# Combinations with Replacement: Cria todas as combinações de tamanho r da lista C, repete os elementos, não altera a ordem.

from itertools import (
    combinations, 
    permutations, 
    product, 
    combinations_with_replacement as combinations_wr
)

def print_iter(iterator):
    print(*list(iterator), sep="\n")

strings = "AB"
pessoas = ["João", "Maria", "Ana", "Pedro"]
camisetas = [["preta", "branca"]]

dados_combinados = pessoas + camisetas

caracteres = "-" * 10
#
#-------------------------------------------------------------------------------
# 1.
print(f"\n{caracteres}ANÁLISE COMBINATORIAL PRODUCT(){caracteres}")

print("\nproduct(), manipulando a lista 'pessoas':")
print_iter(product(pessoas))

print("\nproduct(), manipulando strings com parâmetro 'repeat':")
print_iter(product(strings, repeat=2))

print("\nproduct(), manipulando a lista 'pessoas' e 'camisetas':")
print_iter(product(camisetas, pessoas))
#
#-------------------------------------------------------------------------------
# 2.
print()
print(f"\n{caracteres}ANÁLISE COMBINATORIAL PERMUTATIONS(){caracteres}")

print("\npermutations(), manipulando a lista 'pessoas':")
print_iter(permutations(pessoas, r=2)) # Grupos de 2 pessoas

print("\npermutations(), manipulando strings com parâmetro 'repeat(r)':")
print(list(permutations(strings, r=2)))

print("\npermutations(), manipulando a lista 'pessoas' e 'camisetas':")
print_iter(permutations(dados_combinados, r=2)) # Grupos de 2 pessoas e 2 camisetas
#
#-------------------------------------------------------------------------------
# 3.
print()
print(f"\n{caracteres}ANÁLISE COMBINATORIAL COMBINATIONS(){caracteres}")

print("\ncombinations(), manipulando a lista 'pessoas':")
print_iter(combinations(pessoas, r=2)) # Grupos de 2 pessoas

print("\ncombinations(), manipulando strings com parâmetro 'repeat(r)':")
print(list(combinations(strings, r=2)))

print("\ncombinations(), manipulando a lista 'pessoas' e 'camisetas':")
print_iter(combinations(dados_combinados, r=2)) # Grupos de 2 pessoas e 2 camisetas
#
#-------------------------------------------------------------------------------
# 4.
print()
print(f"\n{caracteres}ANÁLISE COMBINATORIAL COMBINATIONS WITH REPLACEMENT(){caracteres}")

print("\ncombinations_with_replacement(), manipulando a lista 'pessoas':")
print_iter(combinations_wr(pessoas, r=2)) # Grupos de 2 pessoas

print("\ncombinations_with_replacement(), manipulando strings com parâmetro repeat(r):")
print(list(combinations_wr(strings, r=2)))

print("\ncombinations_with_replacement(), manipulando a lista 'pessoas' e 'camisetas':")
print_iter(combinations_wr(dados_combinados, r=2)) # Grupos de 2 pessoas e 2 camisetas
#
#-------------------------------------------------------------------------------
# 5. Product com Desempacotamento
print()
print(f"\n{caracteres}ANÁLISE COMBINATORIAL PRODUCT() DESEMPACOTAMENTO{caracteres}")

camisetas_com_tamanhos = [["preta", "branca"], ["P", "M", "G"], ["Female", "Male"]]
print(*camisetas_com_tamanhos, sep="\n")

print("\nproduct(), manipulando a lista 'camisetas_com_tamanhos':")
print_iter(product(*camisetas_com_tamanhos))