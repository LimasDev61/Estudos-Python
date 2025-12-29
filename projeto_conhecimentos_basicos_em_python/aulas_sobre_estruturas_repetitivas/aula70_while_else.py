# while/else
# recurso exclusivo do Python
# o else é executado quando a condição do while se torna falsa

string = "Valor qualquer"
letra_procurada = "o"
print(string)
procurar = input("Digite a letra que deseja encontrar: ")

i = 0
while i < len(string):
    letra = string[i]
    
    if procurar in letra:
        print(f"a letra procurada '{procurar}' está no indice {i}")

    i += 1
else:
    print("\nFim da busca.") # -> Essa linha é executada quando a condição do while se torna falsa(ao fim da iteração).