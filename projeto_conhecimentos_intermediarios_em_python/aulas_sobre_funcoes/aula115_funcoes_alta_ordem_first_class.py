# Higher Ordem Functions - Funções que recebem outras funções como argumentos ou retornam funções como resultado.
# Exemplos: map, filter, reduce, sorted, etc.
# é uma função de alta ordem quando:
# 1 - Recebe uma ou mais funções como argumento
# 2 - Retorna uma função como resultado
# Closure - função que retorna outra função dentro dela (muito usado em decorators) e chamada também de fecho de função(aninhada).

# função normal
def saudacao(msg):
    return msg

print(saudacao("Olá, Mundo!"))

# Função de alta ordem
def executa_funcao(funcao, valor):
    return funcao(valor) # recebe uma função como argumento e um valor

print(executa_funcao(saudacao, "Olá, Mundo! -> executa a função saudacao com o argumento Olá, Mundo!"))

# Função que retorna outra função - closure
def cria_saudacao(saudacao):
    def saudacao_personalizada(nome):
        return f"{saudacao}, {nome}!"
    return saudacao_personalizada # retorna a função interna

saudacao_oi = cria_saudacao("Oi")
print(saudacao_oi("Maria"))

# Usando funções de alta ordem com listas - map, filter, sorted
nomes = ["Maria", "João", "Ana", "Pedro"]
ordernar_por_tamanho = sorted(nomes, key=len) # ordena por tamanho da string
print(f"Sorted: {ordernar_por_tamanho}") # Ordena a lista por tamanho da string

# Usando map para aplicar uma função a todos os itens de uma lista
def maiusculo(nome):
    return nome.upper()

nomes_maiusculos = list(map(maiusculo, nomes))
print(f"Map: {nomes_maiusculos}") # Aplica a função maiusculo a todos os itens da lista nomes_maiusculos)

# Usando filter para filtrar itens de uma lista
def filtra_nome_com_a(nome):
    return 'a' in nome.lower()

nomes_com_a = list(filter(filtra_nome_com_a, nomes))
print(f"Filter: {nomes_com_a}") # Filtra os nomes que contém a letra 'a'

# Map + Filter juntos
nomes_maiusculos_com_a = list(map(maiusculo, filter(filtra_nome_com_a, nomes)))
print(f"Map + Filter: {nomes_maiusculos_com_a}") # Filtra os nomes que contém a letra 'a' e aplica a função maiusculo


def cumprimentar(pessoas):
    return f"{pessoas}, tudo bem?"

def cumprimentar_todos(nomes, cumprimentar):
    for nome in nomes:
        print(cumprimentar(nome))

nomes = ["Maria", "João", "Ana", "Pedro"]
cumprimentar_todos(nomes, cumprimentar)