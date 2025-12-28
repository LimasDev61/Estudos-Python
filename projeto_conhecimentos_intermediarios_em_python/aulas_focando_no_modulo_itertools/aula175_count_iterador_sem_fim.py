# count é um iterador sem fim(itertools)

# ------------------------------------------------------------------------------

# range(): é um iterável(Sequência) que possui o metodo __iter__(),
# mas não possui o método __next__(). (ao menos que o transformemos em um iterador manual). 

# Obs: Pode se tornar um iterador manualmente caso possua o método iter().
# Não aceita argumentos nomeados, exemplo: range(start=1, stop=10, step=1)
# exemplo:

# lista_range_iter = iter(range(1, 10))

# print(next(lista_range_iter))
# print(next(lista_range_iter))
# print(next(lista_range_iter))

# Saída:
# 1
# 2
# 3

# Sintaxe do range(): range(start, stop, step)

# range(1, 10, 2) -> [1, 3, 5, 7, 9] o step pula de 2 em 2 números.
# range(1, 10) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ------------------------------------------------------------------------------

# count(): é um iterador sem fim(itertools) que possui o método __iter__(),
# e possui o método __next__(). 

# Obs: Ele não possui fim, impossível utilizá-lo sem break(já que ele é infinito e pode consumir
# muita memória). 
# Pode ser utilizado junto a combinação com a função zip do módulo itertools.
# Aceita argumentos nomeados, exemplo: count(start=1, step=2) e permite usar float, diferente 
# do range.

# Exemplo de loop infinito(sem fim):

# Sem o break ou Sem o zip, o terminal roda para sempre e trava.

# for num in count(1, 2):
#     print(num)           

# Sintaxe: count(start, step)
# Sintaxe com float: count(start, step: float)

# count(1, 2) -> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, ...] # Ifinito
# count(1) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...] # Ifinito

# ------------------------------------------------------------------------------

# A diferença de iterador e iteravel:

# O iterável

# É qualquer objeto que podemos colocar em um loop FOR
# Exemplos: listas, tuplas, dicionários, strings, etc.
# Regra: Ele possui o método __iter__(), e automatiza o uso do for devolvendo um iterador.
# Características: Podemos ler quantas vezes quisermos. Se você terminar o objeto iterável
# pode começar do ínicio.

# ------------------------------------------------------------------------------

from itertools import count

# Vamos ver um exemplo de count e range para comparação de iterador e iterável:
count_iterador = count()
range_iteravel = range(10)

print("\ncount_iterador, é um iterável?", hasattr(count_iterador, "__iter__"))
print("count_iterador, é um iterador?", hasattr(count_iterador, "__next__"))
print()
print("range_iteravel, é um iterável?", hasattr(range_iteravel, "__iter__"))
print("range_iteravel, é um iterador?", hasattr(range_iteravel, "__next__"))

# Range é um iterável, mas não é um iterador.

print()

# Exemplo de um range() comum:
print("Range comum, iterável:")
for num in range(10):
    print(num)

# Exemplo de um range() com parâmetros:
print("\nRange com parâmetros, iterável:")
for num in range(1, 10, 2):
    print(num)

# Exemplo de um count() comum:
print("\nCount comum, iterável:")
for num in count():
    print(num)
    if num == 10:
        break

# Exemplo de um count() com parâmetros:
print("\nCount com parâmetros, iterável:")
for num in count(1, 2):
    print(num)
    if num == 11:
        break

# Exemplo de count() com float:
print("\nCount com float, iterável:")
for num in count(1, 2.5):
    print(num)
    if num == 11:
        break

# Exemplo de count() com zip:
print("\nExemplo de count() com zip para gerar IDs em uma lista:")
usuarios = ["Ana", "João", "Maria", "Pedro"]
for id_usuario, nome in zip(count(1), usuarios):
    print(f"{id_usuario} | {nome}")

# Exemplo de count() com a chamada do __next__:
print("\nExemplo de count() com a chamada do __next__ com __iter__:")
contador = count(0, 0.5)
contador_iter = contador.__iter__()
print(contador_iter.__next__()) # 0
print(contador_iter.__next__()) # 0.5
print(contador_iter.__next__()) # 1.0

# Exemplo respeitando a PEP8:
print("\nExemplo respeitando a PEP8 para next():")
print(next(contador)) # 1.5
print(next(contador)) # 2.0
print(next(contador)) # 2.5

# Transformando um iterável em um iterador
print("\nTransformando um iterável em um iterador com o método iter():")
usuarios = ["Ana", "João", "Maria", "Pedro"]
usuarios_iter = iter(usuarios)
print(next(usuarios_iter))
print(next(usuarios_iter))
print(next(usuarios_iter))
print(next(usuarios_iter))


# ------------------------------------------------------------------------------

# A diferença de iterador e iteravel:

# O Iterável

# É qualquer objeto que podemos colocar em um loop FOR
# 
# Exemplos: listas, tuplas, dicionários, strings, etc.
# 
# Regra: Ele possui o método __iter__(), e automatiza o uso do for devolvendo um iterador.
# 
# Características: Podemos ler quantas vezes quisermos. Se você terminar o objeto iterável
# pode começar do ínicio.

# ------------------------------------------------------------------------------

# O Iterador

# É o objeto que faz o trabalho sujo de entregar um valor por vez.

# Como Criar: Criamos um iterador passando um iterável para o método iter(ex: lista).
#
# Regra: Ele possui o método __next__() que é responsável por percorrer cada índice do iterável.

# Características(Perigo): Ele esgota. É como um copo de suco com canudo. Depois que bebemos
# tudo(chegou ao fim), não conseguimos beber de novo. Ficou vazio.