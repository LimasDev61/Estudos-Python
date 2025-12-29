# Exercício - Fatiamento e Len
# Peça para o usuário digitar o nome e a idade
# Se nome e idade forem digitados:
# ..... exiba:
# Seu nome é {nome}
# Seu nome invertido é {nome invertido}
# Seu nome contém(ou não) espaços
# A primeira letra do seu nome é {letra}
# A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade, exiba "Desculpe, você deixou um campo vazio."


nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra do seu nome é: {nome[-1]}")
else:
    print("Desculpe, você deixou um campo vazio.")

tamanho_nome = len(nome)
print(f"O tamanho do seu nome é: {tamanho_nome} caracteres")