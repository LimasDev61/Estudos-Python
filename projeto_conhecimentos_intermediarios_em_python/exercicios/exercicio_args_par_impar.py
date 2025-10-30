# Exercícios com Funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o resultado para uma variável e mostre o valor da variável

# Crie uma função que verifica se um número é par ou ímpar
# Retorne se o número é par ou ímpar

def multiplica_todos_numeros(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def verifica_par_ou_impar(*numeros):
    resultados = []
    for numero in numeros:
        if numero % 2 == 0:
            resultados.append(f"{numero} é Par")
        else:
            resultados.append(f"{numero} é Ímpar")
    return resultados
    

resultado_multiplicacao = multiplica_todos_numeros(1, 2, 3, 4, 5)
print(f"\nResultado da multiplicação: {resultado_multiplicacao}")
print()
verificar_par_impar = verifica_par_ou_impar(10, 20, 30, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, \
                                            62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, \
                                            79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, \
                                            97, 98, 99, 100)
for resultado in verificar_par_impar:
    print(resultado)