# Method vs. @classmethod vs. @staticmethod
#
# ########################################################################################################
#
# Vamos agora consolidar três métodos de classe para entender suas diferenças.
#
# ########################################################################################################
#
# 1. Grande Diferença Técnica
#
# A principal diferença reside no primeiro argumento implícito que o Python passa para a função.
#
# -> Instância: Não tem decorador, e trabalha com o argumento self. O self enxerga todos os atributos do objeto
# e métodos de classe.
#
# -> Classe: Possui o decorador @classmethod, e trabalha com o argumento cls. O cls consegue exengar apenas a
# classe(atributos e outros métodos de classe), mas não enxerga instâncias.
#
# -> Estático: Possui o decorador @staticmethod, não possui argumento de acesso. Ele não enxerga nada da classe
# ou da instância. É uma função isolada e independente.
#
# ########################################################################################################
#
# 2. Comparação por exemplo Real(Backend)
#
# Imagine que estamos construíndo uma classe para gerenciar conexões de Banco de Dados.
#
# Exemplo:

class Database:
    endpoint = "localhost" # Atributo de classe

    def __init__(self, user):
        self.user = user # Atributo de instância

    # 1. Método de Instância: Precisa saber quem é o usuário.
    def connectar(self):
        return f"Conectado ao Banco de Dados do Usuário {self.user}, em {self.endpoint}..."
    
    # 2. Método de Classe: Usado como Factory(Fábrica). Não precisa de um "user" pré-existente para rodar.
    @classmethod
    def configurar_producao(cls):
        cls.endpoint = "10.0.0.1" # Altera para todas as futuras instâncias e atuais.

    # 3. Método Estático: Apenas uma utilidade. Não precisa saber o usuario nem o endpoint.
    @staticmethod
    def validar_ip(ip):
        return len(ip.split(".")) == 4
    
# Testando os Escopos
#
# Uso do Estático(Independente), teste antes de instanciar a classe.
print("\nTestando o escopo estático(@staticmethod) para o IP - 10.0.0.1:\n")
print(Database.validar_ip("10.0.0.1"), "<-- IP Válido") # True
print(Database.validar_ip("10.0.0.1.1"), "<-- IP Inválido") # False

print(20 * "-")

# Uso do Classe(@classmethod), altera o endpoint antes de instanciar a classe.
print("\nTestando o escopo de classe(@classmethod), mudar o endpoint para 10.0.0.1:\n")
print(Database.endpoint, "<-- Endpoint original")
Database.configurar_producao()
print(Database.endpoint, "<-- Endpoint alterado")

print(20 * "-")

# Uso do Instância, precisa saber quem é o usuário.
print("\nTestando o escopo de instância(@instância), precisa saber quem é o usuário:\n")
db = Database("admin")
print(db.connectar(), "<-- Conectado ao Banco de Dados")
# Saída: Conectado ao Banco de Dados do Usuário admin, em 10.0.0.1...

print(20 * "-")
#
# ########################################################################################################
#
# 3. Quando escolher cada um?(Guia de Decisão)
#
# 1. Escolha Método de Instância se: Você precisa acessar ou alterar informações específicas de um objeto
# (ex: salvar um novo nome para o usuário, modificar o saldo de uma conta).
#
# 2. Escolha o @classmethod se: Você está criando algo que age sobre a classe inteira(como um contador de instâncias)
# ou se precisa de multiplas formas de criar um objeto(factories).
#
# 3. Escolha o @staticmethod se: Você de uma função que pertence logicamente àquela classe, mas ela não precisa
# acessar nenhum dado interno(ex: uma função de validação de IP). Serve puramente para limpeza e organização do
# código.
#
# ########################################################################################################
#
# -> Resumo para o Roadmap
#
# Como ja percebemos, o Python é muito flexível. Você poderia fazer tudo com métodos de instância, mas o código
# ficaria sujo. Usar esses decoradores mostra que entendemos os Padrões de Projeto(Design Patterns).
#
# ########################################################################################################
#
# ----- FIM ------
#
# ########################################################################################################
