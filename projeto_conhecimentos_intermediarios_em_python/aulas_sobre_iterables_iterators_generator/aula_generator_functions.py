# Generator Functions - Funções que retornam iteração
# Exemplos: filter, map, reduce, sorted, etc.

# Funções que retornam iteração
# Sintaxe: (expressão for item in list)
# A diferença para o list comprehension é que ele cria um iterator, 
# enquanto o list comprehension cria uma lista

# Exemplo de Generator Function

def quadrados(num):
    for n in num:
        yield n ** 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = quadrados(numeros)

print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
print(next(quadrados))
# print(next(quadrados)) # StopIteration - Exceção

# Fibonacci Generator Function
print("\nFibonacci Generator Function:")
def fibonacci_gen(limite):
    a, b = 0, 1
    contador = 0
    while contador < limite:
        yield a # retorna o valor, pausa a cada iteração
        a, b = b, a + b
        contador += 1

fib_values = list(fibonacci_gen(10))
tamanho = len(fib_values)

for indice, n in enumerate(fib_values):
    print(f"Indice: {indice} - Valor: {n}")
    if indice == tamanho - 1:
        print("Fim da sequência")


# Novo teste
print("\nNovo teste:")
def generator(min=0, max=10):
    while True:
        yield min
        min += 1
        if min == max:
            return

for num in generator():
    print(num)
    
