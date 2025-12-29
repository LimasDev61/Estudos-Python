# operador lógico NOT
# Retorna True se a expressão for falsa
# Retorna False se a expressão for verdadeira

senha_digitada = input('Senha: ')
senha_permitida = senha_digitada =='123456'

if not senha_permitida: # se eu digitar errado a senha ou deixar vazio, vai retornar false que vai ser invertido pelo not e vai entrar no if
    print('Saiu')
else:
    print('Entrou')