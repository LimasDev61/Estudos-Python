# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores em forma de tuplas
# setdefault - adiciona valor se a chave não existe
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
# clear - Apaga todos os itens

# OBS: Métodos que alteram o dicionário sempre retornam None (nada)
dicionario = {'nome': 'Ana', "idade": 25}

# Metodos de Acesso e Verificação

# Get() - Obtém o valor de uma chave, se não existir, retorna None (ou o valor padrão que você passar)
print(dicionario.get("nome"))      # Saída: Ana
print(dicionario.get("idade", 0))  # Saída: 0 (não existe 'idade', então retorna o valor padrão)

print()

# dict.keys() - Retorna um "view object" das chaves
chaves = dicionario.keys()
print(chaves)  # Saída: dict_keys(['nome', 'idade'])
print(f"List: {list(chaves)}")  # Saída: ['nome', 'idade']

print()

# dict.values() - Retorna um "view object" dos valores
valores = dicionario.values()
print(valores)  # Saída: dict_values(['Ana', 25])
print(f"List: {list(valores)}")  # Saída: ['Ana', 25]

print()

# dict.items() - Retorna um "view object" dos itens (chave, valor) - tuplas
itens = dicionario.items()
print(itens)  # Saída: dict_items([('nome', 'Ana'), ('idade', 25)])
print(f"List: {list(itens)}")  # Saída: [('nome', 'Ana'), ('idade', 25)]
for chave, valor in itens:
    print(f"{chave}: {valor}")

print()

# Métodos de Modificação e Atualização

# dict.update() - Atualiza o dicionário com outro dicionário ou com pares chave-valor
# Aceita argumentos nomeados também, exemplo: dicionario.update(nome="Maria", idade=30)
# Aceita também um outro dicionário, exemplo: dicionario.update(outro_dicionario)
# Aceita ambos juntos, exemplo: dicionario.update(nome="Maria", outro_dicionario)
# Se a chave já existir, o valor será atualizado; se não existir, a chave-valor será adicionada
dicionario2 = {"cidade": "São Paulo", "estado": "SP"}
dicionario.update({"nome": "Maria", "altura": 1.65, **dicionario2})
print(dicionario)  # Saída: {'nome': 'Maria', 'idade': 25, 'altura': 1.65, 'cidade': 'São Paulo', 'estado': 'SP'}

print()

# dict.pop() - Remove o item com a chave especificada e retorna o valor
idade = dicionario.pop("idade", None)  # Se não existir, retorna None
print(idade)  # Saída: 25
print(dicionario) # Saída: {'nome': 'Maria', 'altura': 1.65, 'cidade': 'São Paulo', 'estado': 'SP'}

print()

# dict.popitem() - Remove e retorna o último item adicionado (chave, valor)
ultimo_item = dicionario.popitem() # não aceita parâmetro
print(ultimo_item)  # Saída: ('altura', 1.65)
print(dicionario)  # Saída: {'nome': 'Maria', 'cidade': 'São Paulo', 'estado': 'SP'}

print()

# dict.setdefault() - Adiciona um item se a chave especificada não existir
dicionario.setdefault("idade", 0)
print(dicionario)  # Saída: {'nome': 'Maria', 'cidade': 'São Paulo', 'estado': 'SP', 'idade': 0}
dicionario.setdefault("nome", "João")  # Não altera, pois 'nome' já existe
print(dicionario)  # Saída: {'nome': 'Maria', 'idade': 0}

print()

# Atualizar apenas um valor
dicionario["nome"] = "Ana"
print(dicionario)  # Saída: {'nome': 'Ana', 'cidade': 'São Paulo', 'estado': 'SP', 'idade': 0}

print()

# Atualizar por tuplas
dicionario.update([("nome", "Carlos"), ("idade", 28)])
print(dicionario)  # Saída: {'nome': 'Carlos', 'cidade': 'São Paulo', 'estado': 'SP', 'idade': 28}

print()

# Atualizar por listas
dicionario.update([["nome", "Beatriz"], ["idade", 22]])
print(dicionario)  # Saída: {'nome': 'Beatriz', 'cidade': 'São Paulo', 'estado': 'SP', 'idade': 22}

print()

# dict.clear() - Remove todos os itens do dicionário
dicionario.clear()
print(dicionario)  # Saída: {}

print()

# Contagem e Tamanho
dicionario = {'nome': 'Ana', "idade": 25, "cidade": "São Paulo"}
print(len(dicionario))  # Saída: 3 (número de chaves no dicionário)

print()
for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")