# Repetições
# while = enquanto uma condição for verdadeira
# break = para a execução do loop

condicao = True

while condicao:
    nome = input("Qual o seu nome? ")

    if nome == "sair" or nome == "SAIR":
        break


    print(f"Olá {nome}")


print("Acabou")

contador = 0

while contador <= 10:
    print("Contagem para lançar o foguete: ", contador)
    contador += 1


print("Foguete lançado!")
