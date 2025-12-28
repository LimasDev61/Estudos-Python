# Métodos úteis em sets:
# set.add() - Adiciona um elemento ao set, se ele não existir
# set.update() - Adiciona múltiplos elementos ao set (aceita iteráveis), se eles não existirem
# set.remove() - Remove um elemento do set (erro se o elemento não existir)
# set.discard() - Remove um elemento do set (não dá erro se o elemento não existir)
# set.pop() - Remove e retorna um elemento aleatório do set (erro se o set estiver vazio)
# set.clear() - Remove todos os elementos do set
# set.union() - Retorna a união de dois sets (todos os elementos, sem duplicatas). simbolo: |
# set.intersection() - Retorna a interseção de dois sets (apenas elementos comuns). simbolo: &
# set.difference() - Retorna a diferença entre dois sets (elementos no primeiro set que não estão no segundo). simbolo: -
# set.symmetric_difference() - Retorna a diferença simétrica entre dois sets (elementos em ambos os sets, mas não em ambos ao mesmo tempo). simbolo: ^
# set.issubset() - Verifica se um set é subconjunto de outro (todos os elementos do primeiro estão no segundo)
# set.issuperset() - Verifica se um set é superconjunto de outro (todos os elementos do segundo estão no primeiro)
# set.isdisjoint() - Verifica se dois sets não têm elementos em comum (se eles sao disjuntos)
# len(set) - Retorna a quantidade de elementos no set


# Exemplos de Métodos de Adição e Remoção em sets
set1 = {1, 2, 3}
print(f"Set1: {set1}")

# set.add()
set1.add(4) # adiciona o número 4 ao set
print(f"Set1 após add(4): {set1}")

# set.update()
set1.update([5, 6, 7]) # adiciona cada número da lista como elemento separado
print(f"Set1 depois de update([5, 6, 7]): {set1}")
set1.update("abc")  # adiciona cada letra como elemento separado
print(f"Set1 depois de update('abc'): {set1}")
set1.update((8, 9))  # adiciona cada número da tupla como elemento separado
print(f"Set1 depois de update((8, 9)): {set1}")

# Colocar um nome completo como string em um set com update
set1.update(("Renan Silva",))  # adiciona cada palavra da tupla como elemento separado
print(f"Set1 depois de update('Renan Silva'): {set1}")

# set.remove()
set1.remove(3)
print(f"Set1 depois de remove(3): {set1}")
# set.remove() com elemento inexistente gera erro
# set1.remove(10)  # Descomente para ver o erro

# set.discard()
set1.discard(2)
print(f"Set1 depois de discard(2): {set1}")
set1.discard(10)  # Não gera erro, mesmo o elemento não existindo
print(f"Set1 depois de discard(10) (sem erro): {set1}")

# set.pop()
set1.pop()
print(f"Set1 depois de pop(): {set1}")
# set.pop() sem elementos gera erro
# set1.pop()  # Descomente para ver o erro

# set.clear()
set1.clear()
print(f"Set1 depois de clear(): {set1}")

print("\n")
# Exemplos de Métodos de Conjuntos (União, Interseção, Diferença, etc.)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Set1: {set1}")
print(f"Set2: {set2}")
# set.union() ou |
set3 = set1.union(set2) # União dos dois sets
print(f"União (set1 | set2): {set3}")
# ou
# set3 = set1 | set2
# print(f"União (set1 | set2): {set3}")

# set.intersection() ou &
set4 = set1.intersection(set2) # Interseção dos dois sets, procura os itens iguais entre os dois sets
print(f"Interseção (set1 & set2): {set4}")
# ou
# set4 = set1 & set2
# print(f"Interseção (set1 & set2): {set4}")

# set.difference() ou -
set5 = set1.difference(set2) # Diferença entre os dois sets, itens que estão no set1 mas não estão no set2
print(f"Diferença (set1 - set2): {set5}")
# ou
# set5 = set1 - set2
# print(f"Diferença (set1 - set2): {set5}")

# set.symmetric_difference() ou ^
set6 = set1.symmetric_difference(set2) # Diferença simétrica entre os dois sets, itens que não estão em ambos os sets
print(f"Diferença Simétrica (set1 ^ set2): {set6}")
# ou
# set6 = set1 ^ set2
# print(f"Diferença Simétrica (set1 ^ set2): {set6}")

# Métodos de comparação entre sets
setA = {1, 2}
setB = {1, 2, 3}
print(f"SetA: {setA}")
print(f"SetB: {setB}")
# set.issubset() ou <=
print(f"SetA é subconjunto de SetB? {setA.issubset(setB)}") # True, pois todos os elementos de A estão em B
# ou
# print(f"SetA é subconjunto de SetB? {setA <= setB}") # True

# set.issuperset() ou >=
print(f"SetB é superconjunto de SetA? {setB.issuperset(setA)}") # True # pois todos os elementos de A estão em B
# ou
# print(f"SetB é superconjunto de SetA? {setB >= setA}") # True

# set.isdisjoint() ou .isdisjoint()
setC = {4, 5}
print(f"SetC: {setC}")
print(f"SetA e SetC são disjuntos? {setA.isdisjoint(setC)}") # True # pois nenhuma das partes contém elementos em comum

# O que é disjunto?
# Dois conjuntos são disjuntos se não tiverem nenhum elemento em comum.

# Exemplo:
# Conjunto 1: {1, 2, 3}
# Conjunto 2: {4, 5}
# Os conjuntos 1 e 2 são disjuntos, pois nenhuma das partes contém elementos em comum.

print(f"Tamanho(len) de SetB: {len(setB)}") # 3