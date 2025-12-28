# Yield From: Serve para delegar em subgeradores

# Jeito générico de usar yield from
def generator1():
    yield 1
    yield 2
    yield 3


def generator2():
    yield 4
    yield 5
    yield 6

def main_generator():
    yield from generator1()
    yield from generator2()

for value in main_generator():
    print(value)

# Calculo de Fibonacci usando yield from
print("\nFibonacci com yield from:")
def fibonacci_generator_1():
    a, b = 0, 1
    for _ in range(3):
        yield a
        a, b = b, a + b

def fibonacci_generator_2():
    a, b = 5, 8
    for _ in range(3):
        yield a
        a, b = b, a + b

def fibonacci_main_generator():
    yield from fibonacci_generator_1()
    yield from fibonacci_generator_2()

for value in fibonacci_main_generator():
    print(value)

# Valor Retorno
print("\nValor de retorno com yield from:")
def generator_with_return():
    yield 1
    yield 2
    return "Finalizado"

def main_generator_with_return():
    result = yield from generator_with_return() # 
    print("Resultado do generator_with_return:", result)

gen = main_generator_with_return()
try:
    print(next(gen))  # Saída: 1
    print(next(gen))  # Saída: 2
    next(gen)  # Vai levantar StopIteration
except StopIteration as e:
    print("Exceção StopIteration capturada com valor:", e.value)