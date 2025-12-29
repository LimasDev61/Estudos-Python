# Fatiamento de strings objeto (slice) e função len()
# Fatiamento (slice) - Pega uma parte da string
# len() - Quantidade de caracteres da string
# Fatiamento [início:fim:passo] [::passo]

variavel = "Olá, Mundo!"

print(variavel[0:5])  # Olá,  (do índice 0 ao 4)
print(variavel[:12])  # Olá, Mundo!  (do início ao índice 11)
print(variavel[0:])  # Olá, Mundo!  (do índice 0 até o final)
print(variavel[-4])  # d  (índice -4)
print(variavel[:5])  # Olá,  (do início ao índice 4)
print(variavel[4:8]) # , Mun  (do índice 4 ao 7)

print(variavel[-8:-2])  # , Mund  (do índice -8 ao -2)

print(variavel[0:12:1])  # Olá, Mundo!  (do índice 0 ao 11, pulando de 1 em 1)
print(variavel[0:12:2])  # Oá ud!  (do índice 0 ao 11, pulando de 2 em 2)

# Reverter a string
print(variavel[::-1])  # !odnuM ,álO  (do início ao fim, pulando de -1 em -1)
print(variavel[::-2])  # !dM ál  (do início ao fim, pulando de -2 em -2)

# Função len() - Quantidade de caracteres da string
print(len(variavel))  # 11 (quantidade de caracteres da string, começa do 1, não do 0) - é uma contagem, não um índice
print(len(variavel[0:5]))  # 5 (quantidade de caracteres da string fatiada)
print(len(variavel[0:12:2]))  # 6 (quantidade de caracteres da string fatiada com passo 2)
print(len(variavel[::-1]))  # 11 (quantidade de caracteres da string revertida)
print(len(variavel[::-2]))  # 6 (quantidade de caracteres da string revertida com passo -2)
print(len(variavel[::3]))  # 4 (quantidade de caracteres da string com passo 3)

# Outra maneira de escrever a verificação de len, para sempre pegar do início ao fim
print(variavel[0:len(variavel):1])  # Olá, Mundo!  (do índice 0 ao 11, pulando de 1 em 1)
print(variavel[0:len(variavel):2])  # Oá ud!  (do índice 0 ao 11, pulando de 2 em 2)