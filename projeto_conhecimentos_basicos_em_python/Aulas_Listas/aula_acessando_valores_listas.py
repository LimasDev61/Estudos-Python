# Listas de Listas e seus índices

sala = [
    ['Geek1', 'Geek2'], # 0
    ['Geek3',], # 1
    ['Geek5', 'Geek6'], # 2
    ['Geek7', 'Geek8', 'Geek9', ('Geek10', 'Geek11', 'Geek12')] # 3
]

# Acessando valores
print(sala[0]) # ['Geek1', 'Geek2']
print(sala[1]) # ['Geek3']
print(sala[2]) # ['Geek5', 'Geek6']
print(sala[0][0]) # Geek1
print(sala[2][1]) # Geek6
print(sala[1][0]) # Geek3

# Lista com Tuplas
print(sala[3][3]) # ('Geek10', 'Geek11', 'Geek12')
print(sala[3][3][0]) # Geek10

# For
print("\nFor:")
for sala in sala:
    print(f"Sala: {sala}")
    for item in sala:
        print(item)