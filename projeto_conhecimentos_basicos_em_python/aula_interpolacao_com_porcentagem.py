# Interpolação básica de Strings com porcentagem (%)
# %s - String
# %d - Inteiro
# %f - Float
# %x - Hexadecimal
# %o - Octal
# %c - Caractere
# %s - String
# %e - Notação científica

nome = 'Renan'
idade = 30
altura = 1.69

print('Nome: %s, Idade: %d, Altura: %.2f ' % (nome, idade, altura))
print('Nome: %s, Idade: %d, Altura: %.2f ' % ('Maria', 25, 1.75))
print('Nome: %s, Idade: %d, Altura: %.2f' % ('João', 40, 1.80))
print('Nome: %s, Idade: %d, Altura: %.2f' % ('Ana', 22, 1.60))

# com hexadecimal
preco = 1000.50
print('Hexadecimal de %d: é %04x ' % (15, 15))  # 04x - 4 dígitos com zeros à esquerda
print('Hexadecimal de %d: é %04x ' % (255, 255))  # 04x - 4 dígitos com zeros à esquerda
print('Hexadecimal de %d: é %04x' % (4095, 4095))  # 04x - 4 dígitos com zeros à esquerda
print('Hexadecimal de %d: é %04x' % (preco, int(preco)))  # 04x - 4 dígitos com zeros à esquerda
print('Hexadecimal de %d: é %x ' % (10000, 10000))  # x - sem zeros à esquerda
print('Hexadecimal de %d: é %x ' % (65535, 65535))  # x - sem zeros à esquerda
print('Hexadecimal de %d: é %x' % (1048575, 1048575))  # x - sem zeros à esquerda
print('Hexadecimal de %d: é %x' % (preco, int(preco)))  # x - sem zeros à esquerda
print('Preço: %.2f, Hexadecimal: %X' % (preco, int(preco)))  # X - hexadecimal maiúsculo