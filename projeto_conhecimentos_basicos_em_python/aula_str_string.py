"""
Python = Linguagem de Programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos dentro de aspas
"""

# Aspas simples
print('Olá, mundo! Aspas simples')

# Aspas duplas
print("Olá, mundo! Aspas duplas")

# Escape de aspas

# 1. Aspas duplas
print("Olá, \"mundo!\" Aspas duplas Escape")

# 2. Aspas simples
print('Olá, \'mundo!\' Aspas simples Escape')

# 3. Uma barra invertida
print("C:\\Users\\renan\\Desktop\\Python")

# 4. Quebra de linha
print("Linha 1\nLinha 2")

# 5. Tabulacao
print("Linha 1\tLinha 2")

#String Crua(RawString)
print(r"C:\Users\renan\Desktop\Python - String Crua(RawString)")

# F-string
nome = "Renan"
idade = 23
print(f"Olá, {nome}! Sua idade é {idade} anos.")

# Fora de Escape
print("Olá 'Mundo!'") #Aspas Invertidas para simples
print('Olá "Mundo!"') #Aspas Simples para duplas