# groupby - agrupando valores (itertools)

# Regra de Ouro do groupby:
#
# O groupby só consegue agrupar elementros que são vizinhos(consecutivos).
#
# Se a sua lista estiver bagunçada, (A, B, A, A), ele criará 3 grupos: Um para
# o primeiro A, outro para o B, e outro para os A's finais.
#
# Por isso, será obrigado a ordernar(sort) os dados pela mesma chave que usará
# para agrupar.

from itertools import groupby

# Passo 1: Definir a chave de ordenação/agrupamento
def sort_by(students):
    return students["nota"]

students = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# Passo 2: Ordernas os dados(Obrigatório!)
# Sem isso, o groupby não funciona direto.
students.sort(key=sort_by) # ordernar alunos pela nota.

# Passo 3: Agrupar
# O groupby retorna um iterador de tuplas: (chave, grupo_iterador)
group = groupby(students, key=sort_by)

# Passo 4: Exibir
print()
for keys, value in group:
    # A variável "value" é um iterador, Precisamos transformar em uma lista
    print(f"Nota: {keys}")
    for student in value:
        print(f" -> {student['nome']}")
    print("." * 20)


