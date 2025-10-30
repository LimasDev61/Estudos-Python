# Valores padrão para parâmetros
# Ao definir uma função, os parâmetros podem ter um valor padrão
# Caso o valor não seja fornecido, o parâmetro assume o valor padrão

# Funcionamento do None
def saudacao(nome, saudacao_personalizada=None):
    if saudacao_personalizada is None:
        saudacao_personalizada = "Olá"
    print(f"{saudacao_personalizada}, {nome}")


saudacao("Maria") # valor da chamada nome, sem a chamada saudacao_personalizada = None
saudacao("Maria", saudacao_personalizada= "Oi")

# Erros a serem evitados
#def adicionar_item_lista(item, lista_itens = []):
#    lista_itens.append(item)
#    return lista_itens

#   print("\nErro - adiciona itens na mesma lista, função não reutilizada")
#   print(adicionar_item_lista("item 1"))
#print(adicionar_item_lista("item 2"))
#print(adicionar_item_lista("item 3")) # não cria uma nova lista, apenas adiciona os itens na mesma, erro.

# Solucao correta
def adicionar_item_lista(item, lista_itens = None):
    if lista_itens is None:
        lista_itens = []
    lista_itens.append(item)
    return lista_itens

# Cria uma nova lista para cada item.
print("\nSolução correta")
print(adicionar_item_lista("item 1"))
print(adicionar_item_lista("item 2"))
print(adicionar_item_lista("item 3"))