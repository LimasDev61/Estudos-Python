# Closures em lambda.

# Closures em lambda são usadas para criar fábricas de funções.
# Serve para funções personalizadas e On-the-fly functions.
# On-The-fly functions = Funções que podem ser criadas em tempo de execução.

# Exemplo de On-the-fly functions
print((lambda x: x * 2)(5)) 

# Exemplo de fábrica de funções
def criar_multiplicador(multiplicador):
    return lambda x: x * multiplicador

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(5)) # 10
print(triplo(5)) # 15

print("\n")

# Exemplo de closures com reaproveitamento de funções
def executar(funcao, *args):
    return funcao(*args)

somar = executar(lambda m: lambda n: m + n, 20) # executar: funcao
# o valor de somar, sempre será 20 + n, onde m = 20

print(somar(10)) # n = 10 + m = 20 => 30

print("\n")


# Exemplo de closure directamente com lambda
subtrair = lambda m: lambda n: n - m

subtrair_5 = subtrair(5)
subtrair_10 = subtrair(10)

print(subtrair_5(20)) # 15
print(subtrair_10(20)) # 10

print("\n")

# debug via Log com lambda
def executar_debug(funcao, *args):
    print(f"Executando {funcao.__name__} com args={args}")
    resultado = funcao(*args)
    print("Execução concluída")
    return resultado

# Funções criadas com lambda
soma = lambda a, b: a + b
multiplicar = lambda a, b: a * b
potencia = lambda base, exp: base ** exp

# Testes usando a função executar
resultado1 = executar_debug(soma, 10, 5)
resultado2 = executar_debug(multiplicar, 3, 4)
resultado3 = executar_debug(potencia, 2, 8)

print("\nResultados:")
print(f"Soma: {resultado1}")
print(f"Multiplicação: {resultado2}")
print(f"Potência: {resultado3}")
