# For In é uma estrutura de repetição que percorre um elemento iterável (string, lista, tupla, set, dicionário, range)

# Exemplo com string
texto = "Python é a melhor linguagem de programação! Obrigado ao Guido van Rossum por criar essa linguagem incrível!"

for letra in texto:
    print(letra, end='')

texto2 = "Python"
novo_texto = ''

for letra in texto2:
    novo_texto += f'*{letra}'

print("\n" + novo_texto + '*')