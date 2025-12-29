# f-strings servem para formatar strings
# é uma forma mais prática de concatenar strings

# Aula 32 e 46 - Introdução e comandos as f-strings (formatted string literals)

nome = "Renan"
idade = 33
altura = 1.69
peso = 82
reais = 1000000

print(f"{nome} tem {idade} anos, {altura} de altura, {peso} de peso")

# Para formatar com virgula na fração decimal, basta apenas eu acrescentar uma virgula antes do ponto
print(f"Reais: {reais:,.2f}")

# A virgula se encaixa de acordo com sistema decimal milhar/cen/dez/unidade - é chamada de separador de milhar
# No Brasil, o padrão é 1.000.000,00 (ponto para milhar e vírgula para decimal)
# Em outros países, como os Estados Unidos, o padrão é 1,000,000.00 (vírgula para milhar e ponto para decimal)
# No f-string, o padrão é o americano, mas podemos trocar a vírgula pelo ponto e o ponto pela vírgula
# para isso, basta usar o método replace() para substituir os caracteres
print(f"Reais: {reais:,}".replace(",", "."))
print(f"Reais: {reais:,}")

# s - string
print(f"Nome: {nome:s}")  # string

# d - inteiro
print(f"Idade: {idade:d}")  # inteiro

# f - float
print(f"Altura: {altura:.2f}")  # float com 2 casas decimais

# . <número de casas> f - número de casas decimais
print(f"Altura: {altura:.4f}")  # float com 4 casas decimais
print(f"Altura: {altura:.6f}")  # float com 6 casas

# x ou X - hexadecimal (x minúsculo e X maiúsculo)
print(f"Idade em hexadecimal: {idade:x}")  # hexadecimal minúsculo
print(f"Idade em hexadecimal: {idade:X}")  # hexadecimal maiúsculo

# o - octal
print(f"Idade em octal: {idade:o}")  # octal

# c - caractere (converte o número para o caractere correspondente na tabela ASCII)
print(f"Idade como caractere: {idade:c}")  # caractere
print(f"Idade como caractere: {100:c}")  # caractere

# (Caractere especial) - para alinhar o texto, podemos usar o caractere especial < (esquerda), > (direita) e ^ (centro)
# sinal de + ou - para indicar se o número é positivo ou negativo
# Ex.: 0 > 100,.1f - alinha à direita, com 100 caracteres, separador de milhar e 1 casa decimal
print(f"{nome:>10}")  # alinha à direita, com 10 caracteres
print(f"{nome:<10}")  # alinha à esquerda, com 10 caracteres
print(f"{nome:^10}")  # alinha ao centro, com 10 caracteres
print(f"{reais:+.2f}")  # mostra o sinal de + para números positivos
print(f"{-reais:.2f}")  # mostra o sinal de - para números negativos

# Conversion flags - !r (repr), !s (str), !a (ascii)
print(f"{nome!r}")  # usa o método repr() para representar o objeto
print(f"{nome!s}")  # usa o método str() para representar o objeto
print(f"{nome!a}")  # usa o método ascii() para representar o objeto

# Formatação % porcentagem
taxa = 0.05
print(f"Taxa: {taxa:.2%}")  # formata como porcentagem com 2 casas decimais
print(f"Taxa: {taxa:.4%}")  # formata como porcent

# Preenchimento - podemos usar o caractere de preenchimento antes do alinhamento
print(f"{nome:-^20}")  # preenche com - e alinha ao centro, com 20 caracteres

# Preencher com zeros
print(f"{idade:05d}")  # preenche com zeros à esquerda, com 5 caracteres

# Forçar a separação dos numeros, use o =
print(f"{reais:1=+20,.2f}")  # preenche com 1 a esquerda, força o sinal, com 20 caracteres, separador de milhar e 2 casas decimais
print(f"{reais:0=+30,.2f}")  # preenche com zeros a esquerda, força o sinal, com 30 caracteres, separador de milhar e 2 casas decimais

