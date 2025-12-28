import aulas161_packages_init  # Importa o pacote aulas_packages_init

print("\nTestando o pacote aulas_packages_init:")
saudacao = aulas161_packages_init.fala_oi("Olá")  # Acessa a função fala_oi do módulo_init dentro do pacote
print(saudacao("Maria"))  # Chama a função retornada com o nome "Maria"

# Com o __init__.py, dentro do package, ele começa a se comportar como um módulo normal,
# podendo importar funções, classes, variáveis, etc, diretamente do package.
# Note que ao importar o pacote, a mensagem dentro do __init__.py foi exibida,
# indicando que o código dentro do __init__.py foi executado.

# Podemos importar assim também:
# from aulas_packages_init import fala_oi  # Importa diretamente a função fala_oi do pacote
# import aulas_packages_init as api  # Importa o pacote com um alias
# import aulas_packages_init.modulo_init  # Importa o módulo específico dentro do pacote
# Todo o tipo de importação funciona normalmente, graças ao __init__.py
