# Valores Truthy - Imutáveis e Mutáveis

# Decore essa tabela, tudo é Truthy.
"""
# Lista dos Tipos Truthy em Python
============================================================
| Tipo / Categoria       | Valor Truthy                | Exemplo     |
------------------------------------------------------------
| Constante especial      | True                        | True        |
| Numéricos               | 1, 1.0, 1j                   | 1           |
| Sequências / Coleções   | 'a', [1], (1,)               | 'a'         |
| Dicionários e Sets      | {1: 1}, {1}                  | {1: 1}      |
| Booleanos               | True                        | True        |
| Objetos personalizados  | __bool__ → True              | class Obj() |
============================================================
"""

# Exemplos da tabela acima:

# Exemplo de uma lista com itens
dados = [1, 2, 3] # lista com itens (Truthy)

print("Têm itens na lista - mútavel:", bool(dados))
if dados:
    print("Tem itens na lista.")
else:
    print("Não contém itens.")

# Exemplo de um dicionário com itens
print("\n")
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'} # dicionário com itens (Truthy)

print("Têm itens no dicionário - mútavel:", bool(dicionario))
if dicionario:
    print("Tem itens no dicionário.")
else:
    print("Não contém itens.")

# Exemplo de um conjunto com itens
print("\n")
conjunto = {1, 2, 3} # conjunto com itens (Truthy)

print("Têm itens no conjunto - mútavel:", bool(conjunto))
if conjunto:
    print("Tem itens no conjunto.")
else:
    print("Não contém itens.")

# Exemplo de um range com itens
print("\n")
range = range(1) # range com itens (Truthy)

print("Têm itens no range - imutável:", bool(range))
if range:
    print("Tem itens no range.")
else:
    print("Não contém itens.")

# Exemplo de um objeto com dados
print("\n")
__bool__ = True # Objeto com dados (Truthy)

print("Têm dados no objeto - imutável:", bool(__bool__))
if __bool__:
    print("Tem dados no objeto.")
else:
    print("Não contém dados.")

# Valores que contém caracteres e lógica com elementos
# costumam ser Truthy em Python.