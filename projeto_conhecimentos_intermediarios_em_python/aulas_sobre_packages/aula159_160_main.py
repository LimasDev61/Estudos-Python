# Aqui é onde os pacotes serão carregados da pasta aulas_packages
import aulas_sobre_packages.aulas159_160_packages.aula150_160_1_modulo # Importa o módulo criado completo
from aulas_sobre_packages.aulas159_160_packages import aula150_160_1_modulo # Importa o módulo criado
import aulas_sobre_packages.aulas159_160_packages.aula150_160_1_modulo as modulo_principal # Importa o módulo com um alias
from aulas_sobre_packages.aulas159_160_packages.aula150_160_1_modulo import somar # Importa a função somar do módulo
from sys import path

resultado = aula150_160_1_modulo.somar(10, 5)
print(f"O resultado da soma é: {resultado}")

# print("\nCaminhos dos pacotes:")
# print(*path, sep="\n") # desempacotamento para printar cada caminho em uma linha


# Má pratica: importar tudo de um módulo
from aulas_sobre_packages.aulas159_160_packages.aula150_160_1_modulo import *  # Não é recomendado
print(somar(20, 30))  # Usando a função somar importada

# porém, posso também importar apenas o que eu quero do módulo utilizando um
# __all__ no módulo chamado, para todas as vezes que eu utilizar * no módulo, vir apenas
# o que eu quero, assim:
# Vá até o aulas_packages/modulo.py e verifique o que está dentro da lista __all__

print("\nImportando apenas o que está em __all__:")
print(variavel_do_all)  # Variável importada via __all__
# a soma não aparece por não estar dentro do __all__ no módulo

print("\n", __name__)  # Nome do módulo atual

# Chamando a função fala_oi acrescenta no modulo.py
print ("\nTestando a função fala_oi do modulo_oi.py:")
print(aula150_160_1_modulo.fala_oi("Bom dia")("Carlos"))  # Saída: Bom dia, Carlos!

# --- IGNORE ---
# link do motivo de importar com * ser uma má prática:
# https://stackoverflow.com/questions/2386714/why-is-import-bad-practice-in-python

# Para rodar o código, digite no terminal:
# python -m aulas_sobre_packages.aula159_160_main