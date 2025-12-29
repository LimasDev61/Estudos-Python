# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação apropriada. Ex.: Bom dia 0-11, Boa tarde 12-17
# e Boa noite 18-23. Caso o valor informado seja inválido, mostre uma mensagem
# de erro.

hora = input('Que horas são? ')

try:
    hora = int(hora).isdigit()
    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif 18 <= hora <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida, digite um número entre 0 e 23.')
except ValueError:
    print('Isso não é um número inteiro.')


# Exercício Enunciado -> aula 55 e 57 - Saudação conforme a hora do dia