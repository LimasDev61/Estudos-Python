# Try e Except em Python
# Try: bloco de código que pode gerar uma exceção.
# Except: bloco de código que trata a exceção.
# Exceções são classes que representam erros que ocorrem 
# durante a execução do programa.

# Erro Silénciado
a = 18
b = 0
try:
    resultado = a / b
except:
    pass

print("O erro foi silenciado e o programa continua...")

print("\nTratando exceção específica:")
# Tratando exceção específica
try:
    resultado = a / b
except ZeroDivisionError: # Erro de divisão por zero
    print("\nErro: Divisão por zero não é permitida.")
    print("Detalhes do erro:", ZeroDivisionError)
    print("Detalhes do erro:", ZeroDivisionError.__name__)
except TypeError: # Erro de tipo
    print("Erro: Tipo de dado inválido para a operação.")
    print("Detalhes do erro:", TypeError)
    print("Detalhes do erro:", TypeError.__name__)
except NameError: # Erro de nome
    print("Erro: Variável não definida.")
    print("Detalhes do erro:", NameError)
    print("Detalhes do erro:", NameError.__name__)
except Exception as e: # Captura qualquer outra exceção
    print("Erro inesperado:", e)
    print("Detalhes do erro:", type(e).__name__)
# Posso passar tuplas de exceções para um único bloco except
# except (ZeroDivisionError, TypeError) as e:
#     print("Erro de divisão por zero ou tipo inválido:", e)
#     print("Detalhes do erro:", e.__class__.__name__)
# Para verificar o nome do erro, pode-se usar a propriedade __name__ da
#  classe da exceção.
# ou simplesmente criar as váriaveis e resultados fora do bloco try.