# if / elif / else
# se / se não se / se não

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