# Dict Comprehension
# A compreensão de dicionários é usada para criar um novo dict a 
# partir de um iterável, definindo pare chaves-valor de forma expressiva.
import pprint

numeros = [1, 2, 3, 4, 5]
quadrados = {n: n ** 2 for n in numeros}
print(quadrados)


# Exempl de Filtro + Mapeamento com numeros maiores que 5
original = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
filtro_invertido = {v: k for k, v in original.items() if v > 5}
print(filtro_invertido)

produto = {
    "nome": "Caneta Azul", 
    "preco": 2.50,
}

# Mapeamento de dados
confirmar_letras = {chave: valor.upper() if isinstance(valor, str)
                    else valor for chave, valor in produto.items()}

pprint.pprint(confirmar_letras)