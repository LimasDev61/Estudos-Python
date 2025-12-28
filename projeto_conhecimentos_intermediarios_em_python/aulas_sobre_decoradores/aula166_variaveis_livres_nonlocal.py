# Variáveis livres + nonlocal 
# Funções para saber em qual local uma variável está sendo buscada
# Local: dentro da função = locals()
# globals(): nível do módulo (arquivo)

# def fora(x):
#     count = x  # Variável livre
#     def dentro():
#        # print("\n", locals())   # Variáveis locais da função dentro
#        print(dentro.__code__.co_freevars)  # Mostra as variáveis livres
#        return count
#    return dentro

# funcao = fora(10)
# print(funcao())  # 10
# print("\n---\n")

print("Exemplo sem nonlocal:\n")
def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar):
        # valor_final += valor_a_concatenar  # Erro: variável não local, logo não é do escopo
        return valor_final
    return interna

c = concatenar("Olá, ")
print(c("Mundo!"))  # Sempre retornará "Olá, "
print(c("Python!"))  # Sempre retornará "Olá, "

print("\nExemplo com nonlocal:\n")
def concatenar_nonlocal(string_inicial): # Função pai
    valor_final = string_inicial
    def interna(valor_a_concatenar = " "):  # Função interna, com valor padrão
        nonlocal valor_final  # Declara que a variável é não local, ou seja, procure no escopo da função pai
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c_nonlocal = concatenar_nonlocal("Olá, ")
print(c_nonlocal("Mundo!"))  # Retornará "Olá, Mundo!"
final = c_nonlocal()
print(final)  # Retornará ("Olá, Mundo!)

# Resumo Visual
# Termo____________________Onde Procurar?_______________Pode Alterar Valor?
# Variável livre___________Escopo Enclosing(Pai)________Apenas Leitura(Salvo se usar nonlocal)
# Locals()_________________Escopo Local_________________Apenas Leitura(Cópia do estado atual)
# Globals()________________Escopo Global________________Apenas Leitura e Escrita
# nonlocal_________________Escopo Enclosing(Pai)________Permite escrita em variáveis livres

# O Que seria a Escrita em Variáveis Livres:
# Quando uma variável livre de uma função externa(pai) for modificada, isso afeta a variável 
# livre da função interna.
# Mas quando utilizamos o nonlocal, isso afeta diretamente a variável livre da função interna.
# que passa a utilizar a variável livre da função externa(pai).
