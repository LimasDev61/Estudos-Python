# Generator expression
# Uma expressão geradora cria um objeto iteração, mas ele não cria uma lista.
# Ele cria um iterator que pode ser percorrido apenas uma vez.
import sys
# Sintaxe: (expressão for item in list)
# A diferença para o list comprehension é que ele cria um iterator, 
# enquanto o list comprehension cria uma lista, a sintaxe de Generator Expression
# altera de colchetes [] para parenteses ().
# O List Comprehension, trás todos os valores de uma vez e armazena na memória,
# podendo afetar o desempenho do programa.
# enquanto o Generator Expression cria um iterator que pode ser percorrido
# apenas uma vez, executando os valore sob demanda.

# List 
lista = [x ** 2 for x in range(1000)]
print(f"List: {lista}")

print("\nValor total na memória:")
print("Memória ocupada em List Comprehension:")
print(sys.getsizeof(lista), "bytes")

# Generator
print("\nGenerator:")
generator = (x ** 2 for x in range(1000))
for num in generator:
    print("Generator:", num)

print("\nMemória ocupada em Generator:")
print(sys.getsizeof(generator), "bytes")

# Generator Expression tem menor consumo de memória, e tem vantagem
# de performance sobre o List Comprehension, para grandes volumes de dados.

# Com Generator Expression não pode ser acessado por indice
# generator[0] - IndexError.