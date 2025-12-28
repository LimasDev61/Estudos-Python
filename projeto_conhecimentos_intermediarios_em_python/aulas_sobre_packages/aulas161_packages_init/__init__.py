from .aula161_1_modulo_init import fala_oi as fala_oi

print("\nVocê importou o", __name__)

# Em casos de importação no __init__.py, podemos importar com *
# from .modulo_init import *
# Isso permite que ao importar o pacote, todas as funções, classes,
# variáveis, etc, definidas no módulo sejam acessíveis diretamente pelo pacote.