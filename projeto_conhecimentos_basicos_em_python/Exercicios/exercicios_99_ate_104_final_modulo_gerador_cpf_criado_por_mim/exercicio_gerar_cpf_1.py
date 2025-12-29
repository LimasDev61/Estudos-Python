"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# 1. Entrada
cpf_enviado_cliente = "746.824.890-70"
cpf_limpo = cpf_enviado_cliente.replace(".","").replace("-","")

# 2. Processamento - Somar todos os Valores
print("Parte 1 - Soma: ")
soma = 0;
for i, digito in enumerate(cpf_limpo[:9]):
    peso = 10 - i
    soma += int(digito) * peso

print(soma)

# Multiplicar o valor por 10
print("\nParte 2 - Multiplicar por 10: ")
soma *= 10
print(soma)

# Obter o resto da divisão da conta anterior por 11
print("\nParte 3 - Resto da divisão por 11: ")
resultado = soma % 11
print(resultado)

print("\nParte 4 - Resultado: ")
resultado = 0 if resultado > 9 else resultado
print(resultado)

