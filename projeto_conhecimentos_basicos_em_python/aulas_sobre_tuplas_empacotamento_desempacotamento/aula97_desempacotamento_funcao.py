# Desempacotamento em chamadas
# de métodos e funções

string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, "Luiz", "Joaquim"]
tupla = "Python", "é", "legal"

# Referência por posição
print("\nReferência por posição")
print(string[0], string[1], string[2], string[3])

# Desempacotamento comum
print("\nDesempacotamento comum")
primeiro, segundo, *_, terceiro, quarto = lista # <- Isso é uma função de desempacotamento, com o uso do *_
print(primeiro, quarto, terceiro, *_)

# Desempacomento com For
print("\nDesempacotamento com For")
for nome in lista:
    print(nome, end=" ")

# Desempacotamento com *
print("\n")
print("\nDesempacotamento com *:")
print(*string)
print(*lista)
print(*tupla)

# Dicionário

def mostrar(nome, sobrenome):
    print(f"{nome} {sobrenome}")

dicionario = {
    'nome': 'Renan',
    'sobrenome': 'Lima'
}

# Desempacotamento de dicionário
print("\nDesempacotamento de dicionário com **:")
mostrar(**dicionario)

# Desempacotamento Dicionario com *
print("\nDesempacotamento de dicionário com *:")
print(*dicionario)        # mostra só as chaves -> nome sobrenome
print(*dicionario.items()) # mostra tuplas -> ('nome', 'Renan') ('sobrenome', 'Alves') <- Função items() retorna tuplas
print(*dicionario.values()) # mostra só os valores -> Renan Alves <- Função values() retorna os valores
