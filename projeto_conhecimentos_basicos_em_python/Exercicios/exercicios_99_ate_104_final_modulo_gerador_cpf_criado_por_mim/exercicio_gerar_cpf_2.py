"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
    11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
    77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# 1. Entrada
cpf_enviado = "746.824.890-70"
cpf_limpo = cpf_enviado.replace(".","").replace("-","")
segundo_digito = cpf_limpo[:10]
print(segundo_digito)

# 1. Coletando a soma dos 9 primeiros dígitos do CPF

print("\n1 - Coletando a soma dos 9 dígitos do CPF + o primeiro dígito:")
soma = 0
for i, digito in enumerate(segundo_digito):
    peso = 11 - i
    soma += int(digito) * peso

print(soma)

# 2. Multiplicando a soma por 10
print("\n2 - Multiplicando a soma por 10:")
soma *= 10
print(soma)

# 3. Obter o resto da divisão da conta anterior por 11
print("\n3 - Obter o resto da divisão da conta anterior por 11:")
resto = soma % 11
print(resto)

# 4. Se o resultado anterior for maior que 9:
print("\n4 - Se o resultado anterior for maior que 9:")
resultado = 0 if resto > 9 else resto
print(resultado)