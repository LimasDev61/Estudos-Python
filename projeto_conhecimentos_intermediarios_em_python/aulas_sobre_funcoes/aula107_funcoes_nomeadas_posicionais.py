# Argumentos nomeados e não nomeados da função em Python
# Argumentos nomeado tem um nome e um valor
# Argumentos não nomeados tem apenas um valor

# Funções com Retorno
# Argumento não nomeado
def soma(num1, num2):
    return num1 + num2

somas = soma(10, 20)

print(somas)

# Argumento nomeado
def soma2(num1, num2):
    return num1 + num2

somas2 = soma2(num1=10, num2=20)

print(somas2)

# Funções sem retorno
# Argumento não nomeado
def saudar_usuario(nome):
    print(f"Olá, {nome}, bem-vindo(a)!")

saudar_usuario("Maria")

# Argumento nomeado
def saudar_usuario2(nome):
    print(f"Olá, {nome}, bem-vindo(a)!")

saudar_usuario2(nome="Maria")

# Tome cuidado com a ordem dos argumentos, com exceção dos argumentos nomeados

# Argumentos não nomeados sempre vem em primeiro.
# Com argumentos nomeados não importa a ordem dos argumentos.
# Por exemplo:
def saudar_usuario3(nome, sobrenome, hotel):
    print(f"Olá, {nome} {sobrenome}, bem-vindo(a) ao {hotel}!")


saudar_usuario3("Maria", hotel="Marriott", sobrenome="Silva")

# Dentro dos parênteses no def, temos parametros
# Quando chamamos a função com valores, temos argumentos