# O input serve para receber dados do usuario, retornando sempre uma string
nome = input("Qual seu nome? ")
print(f"Olá, {nome}")

idade = input("\nQual sua idade?")
print(f"Você tem {idade} anos") # O retorno vai ser uma string

# Caso queira converter para int
idade = int(input("\nQual sua idade? "))
print(f"Vocé tem {idade} anos convertido para int")

# Caso precisemos converter para float
altura = float(input("\nQual sua altura?"))
print(f"Vocé tem {altura} de altura")

# Caso precisemos converter para booleano
altura = bool(input("\nQual sua altura? "))
print(f"Vocé tem {altura} de altura")

# Caso eu precise fazer um calculo
altura = float(input("\nQual sua altura? "))
peso = float(input("Qual seu peso? "))
imc = peso / (altura / 100) ** 2
print(f"Seu IMC é {imc:.2f}")

# Obtendo o nome da variável na chamada dela
nome = input("\nQual seu nome? ")
print(f"Olá, {nome=}")

# Apesar de eu ter chamado os tipos como função para o input, é uma boa prática
# utilizar o input para receber dados do usuario de forma comum.
# e em seguida fazer a conversão para o tipo correto
# Exemplo:

perguntarIdade = input("\nQual sua idade? ")
idade = int(perguntarIdade)
print(f"Vocé tem {idade} anos")

# Isso permite aumentar a segurança dos dados na hora de receber o que foi digitado pelo usuário
# não quebrando o programa antes de ele ser executado