# Aqui será onde os pacotes serão carregados e instalados
# from . indica que é do mesmo pacote
from aulas161_packages_init import aula161_2_modulo_oi_init # Importa o módulo oi_m do pacote atual
# pode ser usar o . também, para resumir o caminho
# Exemplo: from . import oi_m

__all__ = ["variavel_do_all"]  # Define o que será importado com from modulo import *
# os dados tem que ser passados como string dentro da lista

somar = lambda a, b: a + b

variavel_do_all = "Eu estou dentro do __all__"

# Adicionando a função fala_oi
fala_oi = aula161_2_modulo_oi_init.fala_oi

