# Exemplo de uso dos sets em Python

set1 = set()  # Cria um set vazio
while True:
    letra = input("Digite: ")
    if letra == "0":
        break
    set1.add(letra)  # Adiciona o elemento ao set
    print(set1)
