import aula_modularizacao_2
import sys
# Posso criar meus próprios módulos em Python e adicionar
# ao caminho de busca de módulos
# Útil para projetos grandes, mas falha em deployments, porque
# o caminho de busca de módulos é fixo, então do windows
# para o linux, por exemplo, o caminho pode ser diferente.
# sys.path: serve para manipular os caminhos de busca de módulos em Python.
print("\n")
frase_separada = "ESSE AQUI É O MÓDULO MAIN.PY"
frase_espaçada = " ".join(frase_separada)
print(frase_espaçada)
print("\n")
sys.path.append(r"c:\Users\USUARIO1\Documents\Python - Learning\modulo_personalizado")
try:
    import modulo_python # Está com erro propositalmente para mostrar o exemplo
except ModuleNotFoundError:
    print("Módulo personalizado não encontrado.")

print("Este módulo se chama:", __name__) # __name__ retorna o nome dos módulos importados
print("Caminhos de busca de módulos:", *sys.path, sep="\n") # Mostra os caminhos de busca de módulos

print("\nImportando módulo 3:")
import aula_modularizacao_3
from aula_modularizacao_3 import variavel_modulo
import aula_modularizacao_3 as modulo3_renomeado
from aula_modularizacao_3 import variavel_modulo as var_modulo_renomeada
print("Váriavel do módulo 3 (com prefixo): ", aula_modularizacao_3.variavel_modulo)
print("Váriavel do módulo 3 (importada diretamente, sem prefixo): ", variavel_modulo)
print("Váriavel do módulo 3 (com prefixo via renomeação): ", modulo3_renomeado.variavel_modulo)
print("Váriavel do módulo 3 (importada com renomeação): ", var_modulo_renomeada)