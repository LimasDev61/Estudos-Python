# Flag (Bandeira) - Marca um local no código que pode ser usado para navegação rápida ou referência.
# id -> identificador do objeto
# is -> verifica se o valor e igual
# is not -> verifica se o valor e diferente
# None -> representa a ausência de valor ou um valor nulo

v1 = 'a'

# variaveis pequenas, simples e comuns podem ter a mesma identidade
indentidade_v1 = id(v1)
indentidade_v2 = id('a')
print(f'Identidade de v1: {indentidade_v1}')  # Identidade de v1: (endereço de memória)
print(f'Identidade de v2: {indentidade_v2}')  # Identidade de v2: (endereço de memória)

condicao = False;
passou_no_if = None  # None é um valor especial que representa a ausência de valor

if condicao:
    print('Dentro do if')
    passou_no_if = True
else:
    print('Dentro do else')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

# is verifica se o valor e igual no mesmo local na memória
# is é diferente de == que verifica se o valor é igual, mas não necessariamente no mesmo local na memória