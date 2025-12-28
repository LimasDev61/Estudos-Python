# Retorno de valores das funções (return)

# 1 - Retorno simples

def soma(num1, num2):
    return num1 + num2

somas = soma(10, 20)
print(somas)

# 2 - Erro comum ao retornar valores
def soma2(num1, num2):
    return num1 + num2
    # print("Isso não será executado")  # Código inatingível

somas2 = soma2(10, 20)
print(somas2)

# 3 - Retornando múltiplos valores
def soma_e_subtrai(num1, num2):
    return num1 + num2, num1 - num2 # Empacotamento de tupla

somas, subtracoes = soma_e_subtrai(10, 20) # desempacotamento de tupla
print(somas, subtracoes)

# 4 - Retornando múltiplos valores e atribuindo a uma variável
def soma_e_subtrai2(num1, num2):
    return num1 + num2, num1 - num2 # Empacotamento de tupla
resultado = soma_e_subtrai2(10, 20) # desempacotamento de tupla
print(resultado) # Retorna uma tupla (30, -10)

# 5 - Funções sem return (Valor implicito None)
def saudacao(nome):
    print(f"Olá, {nome}!")

variavel = saudacao("Maria")
print(variavel) # None

# Returns e ifs
def nova_saudacao(nome):
    if nome:
        return f"Olá, {nome}!"
    else:
        return "Olá, estranho!"
    
print(nova_saudacao("João"))
print(nova_saudacao("")) # Retorna "Olá, estranho!"