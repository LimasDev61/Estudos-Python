# Operador lógico "or"
# Retorna True se uma das expressões for verdadeira
# Retorna False se ambas as expressões forem falsas

membro_do_grupo = input('Membro do grupo [S/N]: ')
novo_cliente = input('Novo cliente [S/N]: ')

if membro_do_grupo.upper() == 'S' or novo_cliente.upper() == 'S':
    print('Desconto de 10% aplicado')
else:
    print('Sem desconto')