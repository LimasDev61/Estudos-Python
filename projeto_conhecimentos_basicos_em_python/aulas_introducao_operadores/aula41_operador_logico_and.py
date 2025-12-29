# Operador lógico "and"
# Retorna True se ambas as expressões forem verdadeiras
# Retorna False se uma das expressões for falsa
# Retorna False se ambas as expressões forem falsas

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada.upper() == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')