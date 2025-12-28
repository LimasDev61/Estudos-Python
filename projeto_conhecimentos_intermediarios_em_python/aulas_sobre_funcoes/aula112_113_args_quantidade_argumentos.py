# Args - argumentos não nomeados (quantidade variável de argumentos)
# - * args (empacotamento e desempacotamento)


# Lembre-se do desempacotamento
print("Desempacotamento Comum:")
x, y, *resto = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(x, y)
print(resto)
resto = tuple(resto)
print(resto)

def soma(x, y):
    return x + y

print(soma(1, 2))

# Soma com for * args
def soma_todos_numeros(*args, receber_numeros=None):
    if receber_numeros is None:
        receber_numeros = []

    total = 0
    for numero in args:
        receber_numeros.append(numero)
        total += numero
    return total, receber_numeros # retorna uma tupla

print("\nSoma com for * args")
soma1, numeros1 = soma_todos_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9)
soma2, numeros2 = soma_todos_numeros(1, 2, 3)
print(f"Soma total de {numeros1}:\n{soma1}")
print(f"Soma total de {numeros2}:\n{soma2}")

# Apresentar aluno com strings e *args
def apresentar_aluno(nome, sobrenome, *notas):
    print(f"Aluno: {nome} {sobrenome}")
    print(f"Notas: {notas}, é uma tupla")

print("\nApresentar aluno com strings e *args")
apresentar_aluno("Maria", "Silva", 9.5, 8.1, 7.0, 6.8, 5.9)


# Função Sum
def soma_todos_numeros2(*args):
    print(args) # args é uma tupla
    return sum(args) # função interna sum

print("\nFunção Sum")
soma3 = soma_todos_numeros2(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Soma total: {soma3}")

# Desempacotamento na chamada da função
print("\nDesempacotamento na chamada da função")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9] # lista
soma4 = soma_todos_numeros2(*numeros) # desempacotamento da lista em tupla
print(f"Soma total: {soma4}")