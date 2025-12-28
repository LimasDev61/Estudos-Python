# Problema dos parâmetros mutáveis em funções Python

# Este é um dos tópicos mais recorrentes de bugs no Python. E conhecido como o Problema dos
# Parâmetros Mutáveis com o valor padrão(Default Arguments).

# -> Em resumo: Usar uma lista, dicionários ou qualquer coisa como um objeto Mutável(
# pode ser alterado) como valor padrão de argumentos em uma definição de função(def funcao
# (lista=[])) pode causar comportamentos inesperados.

# 1. A Regra do Problema
#
# Em Python, as funções são objetos. Quando o interpretador(do Python) lê o código e define
# a função(def), ele faz o seguinte:
# - 1. Ele avalia o corpo da função e cria um objeto que representa a função.
#
# - 2. Ele calcula e salva os valores padrão dos argumentos apenas uma vez(no momento da
# definição do script).
#
# Se p valor padrão for um objeto mutável(como uma lista[] vazia), essa mesma lista é usada
# em todas as chamadas subsequentes da função, a menos que passemos uma nova lista como
# argumento.


# 2. Exemplo do Bug Clássico(O Bugzão do Sofrimento)
#
# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista
# 
# cliente1 = adiciona_clientes('luiz')
# adiciona_clientes('Joana', cliente1)
# adiciona_clientes('Fernando', cliente1)
# cliente1.append('Edu')
# 
# Saída: ['luiz', 'Joana', 'Fernando', 'Edu'] (Todos os itens foram adicionados ao cliente_1)
#
# Criando uma segunda Lista:
#
# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# 
# Saída: ["Luiz", "Joana", "Fernando", "Edu", "Helena", "Maria"] (Erro - A segunda lista(cliente2) 
# foi somada a primeira(cliente1).
#   
# Cada chamada, por não ter o segundo argumento, usa a mesma lista única criada na memória,
# fazendo com que o estado persista entre as chamadas.

# 3. A Solução(O Padrão Idiomático)
#
# A solução é garantir que o objeto mutável seja criado do zero toda que a função for chamada.
# Isso é feito usando o valor imutável None como o padrão e criando o objeto mutável dentro do
# corpo da função.
#
# Exemplo(Correto):
#
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = [] # <- Objeto dentro do corpo da Função.
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print("\nLista - Cliente 1:", cliente1)
print("\nLista - Cliente 2:", cliente2)
print("\nLista - Cliente 3:", cliente3)

# 4. Por que None é o escolhido?
#
# None(Falsy) é um valor imutável(não pode ser alterado). Ele é avaliado uma uníca vez na 
# definição da função, mas, como não é alterado, não causa efeitos colaterais.
#
# A condição if list is None: Garante que, se o usuário não fornecer uma lista(com valores Truthy), 
# o código crie uma nova lista limpa a cada execução.
#
# Resumo da Regra:
# 
# Nunca use [], {}, ou instâncias de classes mutáveis como valor padrão de argumento de funções.
# Sempre use o None e inicialize o objeto dentro do corpo da função.