# Contando caracteres em uma string com while

frase = "O Python é uma linguagem de programação incrível!" \
            "E é fácil aprender Python.".lower()

print(frase)

encontrar = input("Digite uma letra para contar quantas vezes ela aparece na frase acima: ")
encontrar_letra_palavra = frase.count(encontrar)

print(f"A letra/palavra '{encontrar}' aparece {encontrar_letra_palavra} vezes na frase acima.")


# Fazendo a mesma coisa com o while
frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)