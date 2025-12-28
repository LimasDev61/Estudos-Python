# Cuidados ao usar recursão em Python:
# Limite de Recursão (Recursion Limit) e Stack Overflow (Estouro de Pilha)
# O limite padrão de recursão em Python é 1000 chamadas.
# Podemos verificar e alterar esse limite importando o módulo sys.
# Mas utilize apenas em casos muito específicos quando tiver certeza do que está fazendo.
# Nunca se esqueça de definir um caso base (condição de parada) para evitar recursões 
# infinitas(Loop Infinito).

import sys

print("\nMódulo SyS - Limite de Recursão (Recursion Limit) em Python")
print("\nLimite de Recursão (Recursion Limit):", sys.getrecursionlimit())

print()
# Alterando o limite de recursão (Recursion Limit)
print("Alterando o Limite de Recursão:\n função -> sys.setrecursionlimit(2000)")
sys.setrecursionlimit(2000)

print("\nNovo Limite de Recursão (Recursion Limit):", sys.getrecursionlimit())

# CUIDADO: Alterar o limite de recursão pode levar a um Stack Overflow (Estouro de Pilha)
# se a recursão for muito profunda. Use com cautela!

print("\n-------------------------------------------------------------")

# Limite de recursão alterado novamente para o padrão - segurança
print("\nRestaurando o Limite de Recursão para o padrão (1000) - Segurança")
sys.setrecursionlimit(1000)

def funcao_fatorial(n):

    if n == 1:
        return 1
    
    return n * funcao_fatorial(n - 1)

print("\nCalculando o fatorial de 5 usando recursão:")
resultado = funcao_fatorial(5)
print(f"O fatorial de 5 é {resultado}")


print("\nCalculando o fatorial de 2001 usando recursão (pode causar Stack Overflow):")
try:
    resultado_grande = funcao_fatorial(2001)
    print(f"O fatorial de 2001 é {resultado_grande}")
except RecursionError:
    print("Erro: Stack Overflow - Limite de Recursão Excedido")