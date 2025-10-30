# Empacotamento e desempacotamento
# *args - argumentos nomeados
# **kwargs - argumentos nomeados

# relembrar...
a, b = 1, 2 # desempacotamento
a, b = b, a # empacotamento
print(a, b) # 2 1

pessoa = {
    "nome": "João",
    "sobrenome": "Silva",
}

dados_pessoa = {
    "idade": 33,
    "cidade": "São Paulo",
}

# Pega os valores das chaves
a, b = pessoa.values() # desempacotamento
print(a, b)

# Pega as Chaves do dicionário
a, b = pessoa # desempacotamento, posso usar o metodo pessoa.keys(), é a mesma coisa.
print(a, b)

# Posso desempacotar internamente
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2) # saida: nome João
print(b1, b2) # saida: sobrenome Silva

# Funciona com for também, sintaxe do enumerate
for chave, valor in pessoa.items():
    print(chave, valor)

# Juntar dois dicionarios dentro de um terceiro
dados_pessoa_juntos = {**pessoa, **dados_pessoa}
print(dados_pessoa_juntos)

# Editando só uma linha do dicionario
dados_pessoa_editada = {**dados_pessoa, "cidade": "DF"}
print(dados_pessoa_editada)

print("\n")

# *args e **kwargs

dicionario_pessoa = {
    "nome": "João",
    "sobrenome": "Silva",
    "idade": 33,
    "cidade": "São Paulo",
}
# Kwargs - argumentos nomeados
# Args - argumentos não nomeados
def mostrar_dados_pessoa(*args, **kwargs):
    print("Argumentos não nomeados:", args)

    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# argumentos nomeados
mostrar_dados_pessoa(1, 3, 4, 6, nome= "João", sobrenome= "Silva", idade= 33, cidade= "São Paulo") # empacotamento no kwargs
mostrar_dados_pessoa(**dicionario_pessoa) # desempacotamento



