# Desempacotamento de um JSON em uma Classe
import json
import os

from aula208_209_exercicio_salve_sua_classe_json import Usuario, CAMINHO_ARQUIVO

with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

os.system("cls")
for pessoas in dados:
    user = Usuario(**pessoas)
    user.status = "Dados voltaram para a Classe Usuario"

    print(f"\nNome: {user.nome}")
    print(f"Cargo: {user.cargo}")
    print(f"Status: {user.status}")

# Prova que os dados voltaram como Instância da classe Usuario
print(f"\nEsse objeto 'user' é do tipo: {type(user)}")
#
# ################################################################################################################
#
# Caso eu queira imprimir os dados pelo FOR:
#
# 1. Criamos uma lista para guardar os objetos recriados
# objetos_recriados = []
#
# for pessoa_dict in dados_json:
#     user = Usuario(**pessoa_dict)
#     # Aqui você modifica o status como desejava
#     user.status = "Dados voltaram para a Classe Usuario"
#     objetos_recriados.append(user)
#
# # 2. Agora percorremos a lista de OBJETOS para imprimir
# for user in objetos_recriados:
#     print("-" * 30)
#     # Usamos vars(user).items() para pegar Chave e Valor do objeto
#     for chave, valor in vars(user).items():
#         print(f"{chave}: {valor}")
#
# Saída:
#
# Nome: Renan Lima
# Cargo: Desenvolvedor
# Status: Dados voltaram para a Classe Usuario
#
# Nome: Maria Lima
# Cargo: Desenvolvedor
# Status: Dados voltaram para a Classe Usuario
#
# Nome: Carlos Lima
# Cargo: Desenvolvedor
# Status: Dados voltaram para a Classe Usuario
#
# ##############################################################################################################
#
# ----- FIM ------
#
# ##############################################################################################################