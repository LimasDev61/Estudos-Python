# Iterável -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vez (next) (__next__)
# next -> function que retorna o próximo valor
# Iter -> function que retorna um objeto iterador

# Iterando em uma string, entregando um objeto na memória
texto = "Python".__iter__()
print(texto)

texto1 = iter(texto) # Mesma coisa que acima
print(texto1)

print(next(texto)) # P
print(next(texto)) # y
print(next(texto)) # t
print(next(texto)) # h
print(next(texto)) # o
print(next(texto)) # n
#print(next(texto)) # StopIteration error

# também podemos fazer de outra forma __next__(texto)
# print(texto.__next__()) # P

# O for faz isso automaticamente para nós
print("\nVersão For:")
for letra in "Python":
    print(letra)

# Se eu fosse fazer com while
print("\nVersão While:")
texto = "Python".__iter__()
while True:
    try:
        letra = next(texto)
        print(letra)
    except StopIteration:
        break

# Assim funciona o FOR por baixo dos panos

# Também podemos passar um objeto iterável para a função iter e ela vai nos devolver um iterador
# Exemplo com range
print("\nExemplo com range:")
numeros = range(10) # range é um iterável (gera números de 0 a 9)
print(numeros)
