# Flag (Bandeira) - Marca um local no código que pode ser usado para navegação rápida ou referência.
# id -> identificador do objeto
# is -> verifica se o valor e igual entre o mesmo local na memória
# is not -> verifica se o valor e diferente entre o mesmo local na memória
# None -> representa a ausência de valor ou um valor nulo
# is é diferente de == que verifica se o valor é igual, mas não necessariamente no mesmo local na memória

# Aula 53 e 54 - ID, is, is not e None

v1 = 'a'

# variaveis pequenas, simples e comuns podem ter a mesma identidade
indentidade_v1 = id(v1)
indentidade_v2 = id('a')
print(f'Identidade de v1: {indentidade_v1}')  # Identidade de v1: (endereço de memória)
print(f'Identidade de v2: {indentidade_v2}')  # Identidade de v2: (endereço de memória)

condicao = False; 
passou_no_if = None  # None é um valor especial que representa a ausência de valor, aqui a flag esta abaixada.

if condicao: # 
    print('Dentro do if')
    passou_no_if = True # Aqui a flag é levantada.
else:
    print('Dentro do else')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')