# Else e Finally em blocos Try Except em Python
# Else: bloco de código que é executado se não houver exceção.
# Finally: bloco de código que é sempre executado, independentemente
# de haver uma exceção ou não.

try:
    resultado = 10 // 2
except:
    print("Erro ao dividir por zero.")
else:
    print("O resultado da divisão é:", resultado)
finally:
    print("O bloco finally sempre é executado.")

# Posso criar a exceção apenas com try e finally
print("\n")
try:
    resultado = 10 / 0
finally:
    print("Bloco finally executado mesmo com erro.")