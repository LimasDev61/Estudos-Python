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
