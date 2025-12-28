# Decoradores com Parâmetros
import functools # Importando modulo functools

# Camada 1: Recebe os parâmetros e retorna outra função que recebe outra função
def decorator(a = None, b = None, c = None): # Fábrica de Decoradores
    # Camada 2: Recebe o decorador real(Função Original)
    def recebe_funcao_decorada(funcao): # Fábrica de Funções
        @functools.wraps(funcao) # Para manter o nome da função original, copiando os metadados
        # Camada 3: Wrapper ele recebe os parâmetros da função original
        def wrapper(*args, **kwargs):
            print(f"Parâmetros: {a}, {b}, {c}")
            return funcao(*args, **kwargs)
        return wrapper
    return recebe_funcao_decorada

# Decorador com os Parâmetros para a função que ele decorar
@decorator(a = 1, b = 2, c = 3)
def sum_numbers(a, b):
    return a + b

params = decorator() # Decorador sem parâmetros, resultado: None, None, None
multiply = params(lambda a, b: a * b)

print(sum_numbers(10, 5))
print(multiply(10, 5))