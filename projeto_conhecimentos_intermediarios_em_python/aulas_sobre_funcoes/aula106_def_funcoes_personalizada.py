"""
Introdução ao def (Definição de Funções) em Python
Funções são trechoes de código usado para
reutilizar um trecho de código em qualquer lugar
do programa.

Elas podem receber valores para parâmetros (argumentos)
e retornar um valor.
Por padrão, funções em Python retornam None(nada).
"""

# Função sem retorno
def saudar_usuario(nome):
    print(f"Olá, {nome}, bem-vindo!")

nome = "senhor"
saudar_usuario(nome)

# None
retorno = saudar_usuario("senhora")
print(retorno) # None, porque a função não retorna nada.

# Função com retorno
def saudar_usuario(nome):
    saudacao = f"Olá, {nome}, bem-vindo!"
    return saudacao

retorno = saudar_usuario("senhora")
print(retorno)