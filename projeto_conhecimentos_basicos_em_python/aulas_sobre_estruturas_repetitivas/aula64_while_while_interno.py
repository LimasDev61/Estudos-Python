# Repetições
# while = enquanto uma condição for verdadeira
# while interno = loop dentro de outro loop


qtd_linhas = 5
qtd_colunas = 5

linha = 1

# Matriz 5x5
while linha <= qtd_linhas:
    print(f'{linha = }')

    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{coluna = }')
        coluna += 1

    linha += 1