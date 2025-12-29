# if / elif / else
# se / se não se / se não

# Aula 36 -> Fluxo do Interpretador para Estruturas Condicionais
# 
# if condição: # vem primeiro se for verdadeiro
# 
# elif condição: # vem depois se for verdadeiro
#
# else: # vem por último se nada for verdadeiro

entrada = input("Você quer entrar ou sair? ")

if entrada == "entrar":
    print("Você entrou no sistema...")
elif entrada == "sair":
    print(" Vocé saiu do sistema...")
else:
    print("Comando desconhecido")

# booleanos
# True -> Verdadeiro
# False -> Falso

if entrada:
    print("Vocé digitou algo")
else:
    print("Vocé digitou vazio")

if not entrada:
    print("Vocé digitou vazio")
else:
    print("Vocé digitou algo")