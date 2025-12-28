# raise - lançando exceções (erros) em Python
# https://docs.python.org/pt-br/3/library/exceptions.html#Exception
# raise: palavra-chave usada para lançar exceções em Python.

def dividir(a, b):
    if b == 0:
        raise ValueError("O denominador não pode ser zero.")
    return a / b

try:
    resultado = dividir(10, 0)
    print("O resultado da divisão é:", resultado)
except (ValueError, ZeroDivisionError) as e:
    if isinstance(e, ValueError):
        print("Erro de valor:", e)
    else:
        print("Erro de divisão por zero:", e)

print("\nOutro exemplo de raise:")
def verificar_idade(idade):
    if not isinstance(idade, (int, float)):
        verificar_tipo = type(idade)
        raise TypeError(f"Idade deve ser um número inteiro, \
                            O tipo fornecido foi: {verificar_tipo.__name__}.")
    elif idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    elif idade < 18:
        raise PermissionError("Menores de 18 anos não têm permissão.")
    return "Pode entrar"

try:
    status = verificar_idade(-5)
    print(status)
except ValueError as e:
    print("Erro de valor:", e)
except PermissionError as e:
    print("Erro de permissão:", e)

try:
    status = verificar_idade(16)
    print(status)
except ValueError as e:
    print("Erro de valor:", e)
except PermissionError as e:
    print("Erro de permissão:", e)

try:
    status = verificar_idade("vinte")
    print(status)
except TypeError as e:
    print("Erro de tipo:", e)

# Exemplo final
# Ideal para caso você queira tratar o erro em outro lugar do código
# ou criar log de erros em algum arquivo.
print("\nExemplo final de raise:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro ao executar a divisão.")
    raise  # Relança a exceção para ser tratada em outro lugar ou 
            #finalizar o programa.