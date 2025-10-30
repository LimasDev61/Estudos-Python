# Closures em Python

# O que são closures?
# Closures ocorrem quando funções internas, definidas dentro de outras funções,
# referenciam variáveis livres do seu escopo. Variáveis livre são as variáveis
# que não são definidas no escopo da função interna(são da função externa).
# Se a função externa retornar apenas a referência da função interna, então
# o interpretador precisará atrelar quaisquer referências a variáveis livres
# que a função interna precisar para que ela possa ser executada fora corretamente.
# São muito usadas em programação funcional, decoradores de função e algoritmos em geral.

def externa(a): # função externa
    # Enclosing, nonlocal, ainda não é closure
    # a é uma variável local da função externa
    def interna(b): # função interna
        # closure
        # Free variable
        return f"{a} {b}" # a é uma variável livre
    return interna # retorna a função interna, sem executá-la

incompleto = externa("Renan") # incompleto recebe a função interna
completo = incompleto(" Lima") # completo executa a função interna

print(incompleto) # <function externa.<locals>.interna at 0x000001E2B3C8B700>
print(completo) # Renan Lima

# Quando usar closures?
# - Para manter estado simples sem usar classes
# - Para criar funções de fábrica (funções que criam outras funções)
# - Para encapsular o código e esconder nomes importantes de escopos amplos
# - Para usar funções de callback (funções que são passadas como argumento para outras funções)
# - Para decoradores (funções que modificam o comportamento de outras funções)
# - Para programação funcional (funções que retornam outras funções)
# - Para evitar o uso de variáveis globais (manter o escopo limpo)

# Exemplo de closure para criar funções de fábrica
def faz_multiplicador(fator):
    def multiplicador(numero):
        return numero * fator
    return multiplicador
dobro = faz_multiplicador(2) # cria a função que multiplica por 2
triplo = faz_multiplicador(3) # cria a função que multiplica por 3
print(dobro(5)) # 10
print(triplo(5)) # 15

# Exemplo de closure para manter estado simples
def contador():
    count = 0
    def incrementar():
        nonlocal count # permite modificar a variável count da função externa
        count += 1
        return count
    return incrementar

cont = contador() # cont recebe a função incrementar
print(cont()) # 1
print(cont()) # 2
print(cont()) # 3

# Exemplo de closure para encapsular código
def saudacao_personalizada(saudacao):
    def cumprimentar(nome):
        return f"{saudacao}, {nome}!"
    return cumprimentar

cumprimentar_ola = saudacao_personalizada("Olá")
cumprimentar_oi = saudacao_personalizada("Oi")
print(cumprimentar_ola("Maria")) # Olá, Maria!
print(cumprimentar_oi("Maria")) # Oi, Maria!

# Exemplo de closure para usar funções de callback
def aplicar_funcao(funcao, valor):
    return funcao(valor)

print(aplicar_funcao(cumprimentar_ola, "João")) # Olá, João!
print(aplicar_funcao(cumprimentar_oi, "João")) # Oi, João!

# Exemplo de closure para evitar o uso de variáveis globais
def gerador_id():
    id_atual = 0
    def proximo_id():
        nonlocal id_atual
        id_atual += 1
        return id_atual
    return proximo_id

novo_id = gerador_id()
print(novo_id()) # 1
print(novo_id()) # 2