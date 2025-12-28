# Função para aumentar o valor dos itens da lista dicionario em 10%
def aumentar_precos(produtos):
    for produto in produtos:
        produto["preco"] = round(produto["preco"] * 1.10, 2)

# Função para ordenar os produtos por nome decrescente
def ordena_por_nome_decrescente(produtos):
    return sorted(produtos, key=lambda x: x["nome"], reverse=True)

# Função para ordenar os produtos por preço crescente
def ordena_por_preco_crescente(produtos):
    return sorted(produtos, key=lambda x: x["preco"])


