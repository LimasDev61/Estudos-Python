# Copy - Serve para criar uma cópia rasa (shallow copy) de um dicionário.
# Cópia rasa significa que ele cria uma nova referência para o dicionário,
# mas se o dicionário contiver objetos mutáveis (como listas ou outros dicionários),
# as alterações nesses objetos mutáveis afetarão ambos os dicionários.
# Copia profunda (deep copy) cria uma cópia profunda de um dicionário,
# criando uma cópia de todos os objetos mutáveis contidos no dicionário,
# garantindo que as alterações nesses objetos não afetem o dicionário original.
import copy

pessoa = {
    "nome": "Renan",
    "sobrenome": "Lima",
    "idade": 33,
    "email": "renanlima@",
    "lista": [1, 2, 3],
}

# Modificando um valor imutável na cópia - não afeta o original
copia_rasa = pessoa.copy()  # Cópia rasa (shallow copy)
copia_rasa["nome"] = "João"
print(pessoa)       # Saída: {'nome': 'Renan', 'sobrenome': 'Lima', 'idade': 33, 'email': 'renanlima@'}

# Modificando um valor mutável na cópia rasa - afeta o original
copia_rasa["lista"].append(4)
print(pessoa)       # Saída: {'nome': 'Renan', 'sobrenome': 'Lima', 'idade': 33, 'email': 'renanlima@', 'lista': [1, 2, 3, 4]}
print(copia_rasa)   # Saída: {'nome': 'João', 'sobrenome': 'Lima', 'idade': 33, 'email': 'renanlima@', 'lista': [1, 2, 3, 4]}

# Usando deepcopy para evitar que alterações em objetos mutáveis afetem o original
copia_profunda = copy.deepcopy(pessoa)  # Cópia profunda (deep copy)
copia_profunda["lista"].append(5)
print(pessoa)       # Saída: {'nome': 'Renan', 'sobrenome': 'Lima', 'idade': 33, 'email': 'renanlima@', 'lista': [1, 2, 3, 4]}
print(copia_profunda)   # Saída: {'nome': 'Renan', 'sobrenome': 'Lima', 'idade': 33, 'email': 'renanlima@', 'lista': [1, 2, 3, 4, 5]}

# Resumo:
# - Use copy() para criar uma cópia rasa quando o dicionário contém apenas valores imutáveis.
# - Use copy.deepcopy() para criar uma cópia profunda quando o dicionário contém objetos mutáveis.
# - Entenda a diferença entre cópia rasa e cópia profunda para evitar efeitos colaterais indesejados.
# --- IGNORE ---