# Recarregar módulos usando importlib e comportamento singleton
# O importlib permite recarregar módulos que já foram importados
# Isso é útil durante o desenvolvimento, quando você faz alterações
# em um módulo e quer ver essas mudanças refletidas sem reiniciar o
# programa inteiro.
# Importante: Módulos em Python são singletons por padrão, ou seja,
# quando um módulo é importado, ele é carregado na memória apenas uma vez.
# Isso significa que se vocé recarregar um módulo, ele vai ser carregado
# novamente, mesmo se ele já foi carregado anteriormente.
# Isso pode causar problemas se vocé estiver trabalhando com módulos
# que dependem de outros módulos, pois eles serão carregados novamente
# e o resultado pode ser diferente do que vocé esperava.
# Para evitar esse problema, vocé pode usar o importlib para recarregar
# módulos sem reiniciar o programa inteiro.
# Singleton: Um módulo é carregado apenas uma vez na memória,
# mesmo que seja importado várias vezes.
# importlib: Módulo que permite recarregar módulos já importados.

import importlib # Importa o módulo importlib para recarregar módulos
import aula_recarregando_modulos_importlib_singleton_2 # Singleton, só importa uma vez


print (aula_recarregando_modulos_importlib_singleton_2.__name__)
print("Primeira importação concluída.")

# Teste do recarregamento do módulo
importlib.reload(aula_recarregando_modulos_importlib_singleton_2)
print("Módulo recarregado.")

# Só vai ser exibido após o recarregamento do módulo
print(aula_recarregando_modulos_importlib_singleton_2.variavel)