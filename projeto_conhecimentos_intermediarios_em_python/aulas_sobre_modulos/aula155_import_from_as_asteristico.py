# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html

# 1. import(importação padrão de módulos) 
# sintaxe: import nome_do_módulo
# acesso: Você precisa usar o nme do módulo como 
# prefixo para acessar qualquer coisa dentro dele.

# exemplo: 
# import math
# raiz = math.sqrt(16)
# pi = math.pi
# print("A raiz quadrada de 16 é:", raiz)
# print("O valor de pi é:", pi.__round__(3))

# 2. from... import (importação específica de módulos)
# sintaxe: from nome_do_módulo import nome_da_função_ou_variável
# acesso: Acessamos o item diretamente pelo nome, sem o prefixo do módulo.

# exemplo:
# from math import sqrt, pi
# raiz = sqrt(16)
# print("A raiz quadrada de 16 é:", raiz)
# print("O valor de pi é:", pi.__round__(3))

# 3. import... as (importação padrão de módulos com apelidos)
# sintaxe: import nome_do_módulo as apelido ou from modulo import item as apelido
# acesso: Usamos o apelido para acessar o módulo ou item.
# uso: É comum para módulos com nomes longos (ex: numpy -> np) para evitar conflitos de
# nomes.

# exemplo 1:
# import math as m
# raiz = m.sqrt(16)
# print("A raiz quadrada de 16 é:", raiz)
# print("O valor de pi é:", m.pi.__round__(3))

# exemplo 2:
# from math import sqrt as raiz_quadrada, pi as valor_pi
# raiz = raiz_quadrada(16)
# print("A raiz quadrada de 16 é:", raiz)
# print("O valor de pi é:", valor_pi.__round__(3))

# 4. from... import * (importação de todos os itens de um módulo)
# sintaxe: from nome_do_módulo import *
# acesso: Acessamos o item diretamente pelo nome, sem o prefixo do módulo.
# uso: Não é recomendado, pois pode causar conflitos de nomes e dificultar 
# a leitura do código.
# cuidado: Geralmente, ele deve ser evitado! pois ele pode levar a conflitos de nomes
# (se dois módulos tiverem uma função chamada log(), por exemplo) e tornar o código menos
# claro sobre a origem dos itens importados.

# exemplo:
# from math import *
# raiz = sqrt(16)
# print("A raiz quadrada de 16 é:", raiz)
# print("O valor de pi é:", pi.__round__(3))

# Se tivessemos outra função pi() em outro módulo importado com *,
# poderia haver um conflito de nomes, levando a erros difíceis de depurar.

# A regra geral em Python é:

"""
1. Use import quando quiser importar (ex: import math) como padrão.
É a forma mais clara de ver de onde os itens vêm.

2. Use from... as (ex: import numpy as np) é util para apelidar nomes longos.

3. Use from... import (ex: from math import sqrt) para importar itens específicos,
caso precisemos de uma ou duas coisas que quisermos evitar o prefixo do módulo.

4. Evite from... import * sempre que possível para manter o código claro e evitar 
conflitos de nomes.
"""
