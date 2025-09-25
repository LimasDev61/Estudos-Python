# Sep - separador serve para separar os argumentos com um determinado caractere ou não.
print(12, 34, 56, sep= " - ", end=" - ")


# Quebra de linha com padrão CRLF
# no Windows 11, não precisamos utilizar \r\n juntos, podemos optar por apenas \n
print(15, 45, 60, sep= " - ", end="\n")
print(13, 35, 57, sep= " - ", end="\r\n")

#Podemos usar o end para colocar um texto na mesma linha que a quebra de linha, colocando uma string como argumento
print("Hoje é sexta-feira", end=". ")
print("Vamos estudar Python")