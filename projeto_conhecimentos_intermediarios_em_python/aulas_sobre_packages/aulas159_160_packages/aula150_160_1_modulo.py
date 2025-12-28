# Aqui será onde os pacotes serão carregados e instalados
# from . indica que é do mesmo pacote
from aulas_sobre_packages.aulas159_160_packages import aula159_160_2_modulo_oi as oi_m  # Importa o módulo oi_m do pacote atual
# pode ser usar o . também, para resumir o caminho
# Exemplo: from . import oi_m

__all__ = ["variavel_do_all"]  # Define o que será importado com from modulo import *
# os dados tem que ser passados como string dentro da lista

somar = lambda a, b: a + b

variavel_do_all = "Eu estou dentro do __all__"

# Adicionando a função fala_oi do módulo oi_m
fala_oi = oi_m.fala_oi