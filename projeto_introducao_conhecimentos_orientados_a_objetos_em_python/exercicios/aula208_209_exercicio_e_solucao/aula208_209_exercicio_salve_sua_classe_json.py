# Exercício - Salve sua Classe em JSON
# Salve os dados da sua classe JSON e depois crie novamente as instâncias.
# da classe com os dados salvos.
# Faça em arquivos separados.

# Aula 208: Exercício - Salve sua Classe em JSON
# Aula 209: Solução - Exercício + if___name__ == '__main__'

# ################################################################################################################
#
# Solução:
#
import json
import os

# Só funciona para arquivos no mesmo diretório:
#
# 1. Descobre o caminho da pasta onde este arquivo .py está salvo(mesma pasta)
BASE_DIR = os.path.dirname(__file__)
#
# 2. Une esse caminho com a pasta e o arquivo que você quer(aula208_209... + salvando_arquivo_json/usuarios.json)
# Isso cria um caminho absoluto como: C:\Users\...\salvando_arquivo_json\usuarios.json
CAMINHO_ARQUIVO = os.path.join(BASE_DIR, "salvando_arquivo_json", "usuarios.json")
#
#
class Usuario:
    def __init__(self, nome, cargo, status = None):
        self.nome = nome
        self.cargo = cargo

        self.status = "Dados Iniciado"

    def transformar_dados_em_dicionario(self):
        self.status = "Dados Transformados em JSON"
        return vars(self)
        

p1 = Usuario("Renan Lima", "Desenvolvedor")
p2 = Usuario("Maria Lima", "Desenvolvedor")
p3 = Usuario("Carlos Lima", "Desenvolvedor")

print("\nP1: ", p1.status)
print("P2: ", p2.status)
print("P3: ", p3.status)

dados = [p.transformar_dados_em_dicionario() for p in [p1, p2, p3]]

if dados:
    print("\nP1, P2, P3:", p1.status)

def criar_dump(caminho_arquivo, dados_lista):
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados_lista, arquivo, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    criar_dump(CAMINHO_ARQUIVO, dados)
    if dados:
        print("\nDADOS SALVOS COM SUCESSO!\n")

        print(f"Caminho: {CAMINHO_ARQUIVO}")
#
# ################################################################################################################
#
# 1. Usando status=None (O mais recomendado)
#
# Use quando você sabe quais campos podem vir no seu JSON e quer ter controle sobre eles.
#
# Vantagem: É explícito. Quem lê sua classe sabe exatamente o que ela armazena (nome, cargo e status).
#
# Segurança: Se o JSON vier com um erro de digitação (ex: "statuuuus"), o Python ainda vai dar erro, o que te ajuda a 
# encontrar bugs rapidamente na sua maquina-desenvolvimento.
# 
# Exemplo:
# 
# class Usuario:
#     def __init__(self, nome, cargo, status=None):
#         self.nome = nome
#         self.cargo = cargo
#         self.status = status
#
# ################################################################################################################
#
# 2. Usando **kwargs (Flexibilidade Extrema)
#
# Use quando você não tem controle total sobre o que vem no JSON ou quando o JSON tem dezenas de campos e você só 
# se importa com alguns.
#
# Vantagem: Sua classe nunca quebra por "argumento inesperado". Ela aceita qualquer coisa.
#
# Desvantagem: O Python "engole" campos extras e você pode nem perceber que seu JSON está vindo com lixo ou dados 
# desatualizados.
#
# Exemplo:
#
# class Usuario:
#     def __init__(self, nome, cargo, **kwargs):
#         self.nome = nome
#         self.cargo = cargo
#         self.status = kwargs.get("status")
#
# ################################################################################################################
#
# ----- FIM ------
#
# ################################################################################################################