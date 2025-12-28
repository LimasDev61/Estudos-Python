# Importações das funções do módulo produtos_modulo
from packages_modulares.produtos_modulo import aumentar_precos, ordena_por_nome_decrescente \
    , ordena_por_preco_crescente
import copy

# Exercícios modulados
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print("\nProdutos originais:")
print(*produtos, sep='\n')

novos_produtos = copy.deepcopy(produtos)
aumentar_precos(novos_produtos)

print("\nProdutos com preços aumentados em 10%:")
print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

print("\nProdutos ordenados por nome decrescente:")

produtos_ordenados_por_nome = copy.deepcopy(ordena_por_nome_decrescente(produtos))
print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print("\nProdutos ordenados por preço crescente:")
produtos_ordenados_por_preco = copy.deepcopy(ordena_por_preco_crescente(produtos))
print(*produtos_ordenados_por_preco, sep='\n')
