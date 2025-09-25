# Introdução ao tratamento de exceções em Python
# try: Tenta executar o código
# except: Executa se der erro no try
# else: Executa se não der erro no try
# finally: Sempre executa, independente se deu erro ou não

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    resultado = num1 / num2
    print(f"O resultado é {resultado}")

except ZeroDivisionError:
    print("Deu algum erro, tente novamente.")
except ValueError:
    print("Valor inválido, digite apenas números.")
except Exception:
    print("Erro desconhecido.")
else:
    print("Executa quando não ocorre erro.")
finally:
    print("Sempre executa, erro ou não.")