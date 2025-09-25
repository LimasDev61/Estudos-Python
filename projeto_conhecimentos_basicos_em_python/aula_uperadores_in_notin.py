# Operadores "in" e "not in"
# "in" verifica se um valor está presente em uma sequência (como listas, tuplas, strings)
# "not in" verifica se um valor não está presente em uma sequência
# Strings são iteráveis(ite vem de item), ou seja, podemos percorrer cada caractere individualmente

nome = "Renan Alves da Silva Lima"
numeros = [1,2,3,4,5,6,7,8,9,0]

# indice acessado de forma comum
print(nome[0])  # R
print(nome[7])  # A
print(nome[-1])  # A
print(nome[-2])  # M
print(nome[0:3])  # Ren
print(nome[5:])  # Alves da Silva Lima
print(nome[5:-1])  # Alves da Silva Lima
print(nome[:5])  # Renan
print(nome[::2])  # RnaAes lSvS lMa

# Agora com o operador "in" && "not in"
print('R' in nome)  # True
print('A' in nome)  # True
print('A' not in nome)  # False # False porque o A está no nome
print('Renan' in nome)  # True
print('Renan' not in nome)  # False # False porque o Renan está no nome
print('renan' in nome)  # False # False porque o renan está com r minúsculo e o nome tem R maiúsculo
print('Silva' in nome)  # True
print('Silva' not in nome)  # False # False porque o Silva está no nome
print('Silva' in nome[10:])  # True # True porque o Silva está no nome a partir do índice 10
print('Silva' in nome[15:])  # False # False porque o Silva não está no nome a partir do índice 15
print('Silva' in nome[:15])  # True # True porque o Silva está no nome até o índice 15
print('Silva' in nome[:10])  # False # False porque o Silva não está no nome até o índice 10
print('Silva' in nome[5:15])  # True # True porque o Silva está no nome entre os índices 5 e 15
print('Silva' in nome[5:10])  # False # False porque o Silva não está no nome entre os índices 5 e 10
print('Silva' in nome[10:20])  # True # True porque o Silva está no nome entre os índices 10 e 20
print('Silva' in nome[10:15])  # False # False porque o Silva não está no nome entre os índices 10 e 15
print('Silva' in nome[15:20])  # True # True porque o Silva está no nome entre os índices 15 e 20
print('Silva' in nome[20:])  # False # False porque o Silva não está no nome a partir do índice 20
print('Silva' in nome[:20])  # True # True porque o Silva está no nome até o índice 20
print('Silva' in nome[:15])  # True # True porque o Silva está no nome até o índice 15
print('Silva' in nome[:10])  # False # False porque o Silva não está no nome até o índice 10
print('Silva' in nome[:5])  # False # False porque o Silva não está no nome até o índice 5
print('Silva' in nome[::2])  # False # False porque o Silva não está no nome quando pulamos de 2 em 2
print('Silva' in nome[::3])  # False # False porque o Silva não está no nome quando pulamos de 3 em 3
print('Silva' in nome[::4])  # False # False porque o Silva não está no nome quando pulamos de 4 em 4
print('Silva' in nome[::5])  # True # True porque o Silva está no nome quando pulamos de 5 em 5
print('Silva' in nome[::6])  # False # False porque o Silva não está no nome quando pulamos de 6 em 6

print(1 in numeros)  # True
print(10 in numeros)  # False
print(10 * '-' in numeros)  # True # True porque o 10*- está presente na string numeros

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'Encontrado {encontrar} em {nome}')
else:
    print(f'Não encontrado {encontrar} em {nome}')

if ' ' in nome:
    print('Seu nome tem espaço')
else:
    print('Seu nome não tem espaço')
