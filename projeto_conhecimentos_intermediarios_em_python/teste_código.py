
import decimal

# Exemplo 1 - FORMAT FSTRING
numer_1 = 0.1
numer_2 = 0.2
resultado = numer_1 + numer_2
print("Resultado com format fstring: ", f"{resultado:.17f}")

# Exemplo 2 - ROUND - arredondador do banqueiro
print("\nResultados com round: ")
print(round(3.14159, 2))
print(round(3.14759, 2))
print(round(3.5))
print(round(2.5)) # Arrendonda para o par mais próximo

# Exemplo 3 - DECIMAL
print("\nResultados com decimal: ")
print(decimal.Decimal("3.14159").quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
print(decimal.Decimal("3.14500").quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)) 
print(decimal.Decimal("3.5").quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
print(decimal.Decimal("2.5").quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))

# Exemplo 4 - Decimal GetContext
print("\nResultados com decimal: ")
valor1 = decimal.Decimal("3.14159")
valor2 = decimal.Decimal("3.14759")
decimal.getcontext().prec = 10
total = valor1 + valor2
print(total)