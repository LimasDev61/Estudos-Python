# Escopo de funções em Python
# Escopo significa o local onde a variável foi declarada.
# O escopo global é o escopo do arquivo, que significa que a variável pode ser usada em qualquer parte do programa.
# O escopo local é o escopo da função, que significa que a variável só pode ser usada dentro da função.
# Variáveis declaradas dentro de uma função são locais e não podem ser acessadas fora da função.

# Escopo global
variavel_global1 = 40

def funcao():
    # Escopo local
    variavel_local = 20
    print(f"Variável local: {variavel_local}")
    print(f"Variável global dentro da função: {variavel_global1}")

funcao()

# Variável global
print("\nVariável global dentro da função: ")
variavel_global2 = 50
print(f"Variável global antes de chamar a função: {variavel_global2}")

def funcao_correta():
    global variavel_global2  # Declara que queremos usar a variável global
    variavel_global2 = 60    # Modifica a variável global
    print(f"Variável global modificada dentro da função: {variavel_global2}")


funcao_correta()

# Escopo Enclosing(Aninhado)
print("\nEscopo Enclosing(Aninhado): ")
x = 10;

def escopo():
    x = 13

    def escopo_interno():
        x = 11
        y = 2
        print(f"Escopo interno: {x}, {y}")
    escopo_interno()
    print(f"Escopo externo: {x}")

escopo()
print(f"Escopo global: {x}")

# Erro - variável local
print("\nErro - variável local: ")
contagem = 0
def incrementar_error():
    contagem = contagem + 1  # Isso cria uma nova variável local 'contagem'
    return contagem

incrementar_error()  # Isso causará um erro porque a variável local 'contagem' não foi inicializada

# Global é uma má prática