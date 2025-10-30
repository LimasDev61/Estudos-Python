# ValorFalsy, Tipos Mutáveis e Imutáveis

# Decore essa tabela, tudo fora dela é Truthy.
"""
# Lista dos Tipos Falsy em Python
============================================================
| Tipo / Categoria       | Valor Falsy                 | Exemplo     |
------------------------------------------------------------
| Constante especial      | None                        | None        |
| Numéricos               | 0, 0.0, 0j                  | 0           |
| Sequências / Coleções   | '', [], (), range(0)         | []          |
| Dicionários e Sets      | {}, set()                    | {}          |
| Booleanos               | False                        | False       |
| Objetos personalizados  | __bool__ → False             | class Obj() |
============================================================

Observação:
    Qualquer valor "vazio" ou equivalente a zero é considerado Falsy em Python.
"""


# Exemplos da tabela acima:

# Exemplo de uma lista vazia
dados = [] # lista vazia(Falsy)

print("Têm itens na lista - mútavel:", bool(dados))
if dados:
    print("Tem itens na lista.")
else:
    print("Não tem itens na lista.")

# Exemplo de uma string vazia
print("\n")
string = "" # string vazia(Falsy)

print("Têm caracteres na string - imutável: ", bool(dados))
if string:
    print("Contém caracteres.")
else:
    print("Não contém caracteres.")

# Exemplo de um dicionário vazio
print("\n")
dicionario = {} # dicionário vazio(Falsy)

print("Têm itens no dicionário - mútavel:", bool(dicionario))
if dicionario:
    print("Têm dados no dicionário.")
else:
    print("Não tem dados no dicionário.")

# Exemplo de um conjunto vazio
print("\n")
conjunto = set() # conjunto vazio(Falsy)

print("Têm itens no conjunto - mútavel:", bool(conjunto))
if conjunto:
    print("Têm dados no conjunto.")
else:
    print("Não tem dados no conjunto.")

# Exemplo de um range vazio
print("\n")
range = range(0) # range vazio(Falsy)

print("Têm itens no range - imutável:", bool(range))
if range:
    print("Têm dados no range.")
else:
    print("Não tem dados no range.")

# Exemplo de um booleano vazio
print("\n")
booleano = False # booleano vazio(Falsy)

print("Têm itens no booleano - imutável:", bool(booleano))
if booleano:
    print("Têm dados no booleano.")
else:
    print("Não tem dados no booleano.")

# Exemplo de um objeto vazio
print("\n")
objeto = None # objeto vazio(Falsy)

print("Têm itens no objeto - imutável:", bool(objeto))
if objeto:
    print("Têm dados no objeto.")
else:
    print("Não tem dados no objeto.")

# Exemplo de um objeto personalizado
print("\n")
__bool__ = False # objeto personalizado vazio(Falsy)

print("Têm itens no objeto - imutável:", bool(__bool__))
if __bool__:
    print("Têm dados no objeto.")
else:
    print("Não tem dados no objeto.")
