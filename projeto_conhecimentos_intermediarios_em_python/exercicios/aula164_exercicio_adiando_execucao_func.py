# Exercício - adiando a execução de uma função

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

# Erro do modelo do código proposto:
# def criar_funcao(funcao, *args):
#     return funcao(*args)
# Esse erro proposital acontece porque a função criada já executa a função
# passada como argumento, e não adianta a execução.

# resolução correta, para somar e multiplicar sempre por um valor fixo:
def criar_funcao(funcao, x):
    def funcao_interna(y):
        return funcao(x, y)
    return funcao_interna

# valor fixo de soma: 2
somar = criar_funcao(soma, 2)

# valor fixo de multiplicação: 5
multiplicar = criar_funcao(multiplica, 5)

print("O resultado da soma de 2 + 5 é:", somar(5))
print("O resultado da multiplicação de 5 x 10 é:", multiplicar(10))

# com *args

# resolução correta, para somar e multiplicar com quaisquer valores:
print("\nCom *args:")
def criar_funcao_args(funcao, *args):
    def funcao_interna():
        return funcao(*args)
    return funcao_interna

soma_args = criar_funcao_args(soma, 3, 7)
multiplica_args = criar_funcao_args(multiplica, 4, 6)

print("O resultado da soma de 3 + 7 é:", soma_args())
print("O resultado da multiplicação de 4 x 6 é:", multiplica_args())
