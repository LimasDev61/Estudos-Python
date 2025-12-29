# .format para formatar strings é utilizando em versões anteriores ao python 3.6
nome = "Renan"
idade = 33
altura = 1.69

totalPessoas = 10000000
totalDesistentes = 1000

# Exemplo Básico
mensagem = "{}, {}, {}".format(nome, idade, altura)
print(mensagem)

# Exemplo por indicies
mensagem = "{2}, {1}, {0}".format(nome, idade, altura)
print(mensagem)

# Exemplo por nome de variavel passadas como argumento
mensagem = "{n}, {i}, {a}".format(n=nome, i=idade, a=altura)
print(mensagem)

# Exemplo númericos de formatação
mensagem = "{0:.2f}, {1:.2f}".format(totalPessoas, totalDesistentes)
print(mensagem)

# Exemplo númericos de formatação com separador de milhar
mensagem = "{0:,}, {1:,}".format(totalPessoas, totalDesistentes)
print(mensagem)
