# Aula 223, Parte 1: Super e a sobreposição de membros em Python OOP
# Aula 224, Parte 2: Super e a sobreposição de membros em Python OOP
#
# ################################################################################################################
#
# Na Engenharia de Software, a sobre de membros(Override) e o uso da função super() são ferramentas que permitem o
# equilíbrio perfeito entre reaproveitamento e customização.
#
# Equanto a sobreposição permite que a classe filha "mude as regras", o super() garante que não precise reescrever
# a lógica que o "pai" já faz bem.
#
# ################################################################################################################
#
# 1. Sobreposição de Métodos (Method Overriding)
#
# A sobreposição ocorre quando uma subclasse define um método com o mesmo nome de um método da superclasse. Quando
# chamamos esse método em um objeto da classe filha, o Python executa a versão da filha, "escondendo" a versão da pai.
#
print("\nSobreposição de Métodos (Method Overriding):\n")
class Notificacao:
    def enviar(self):
        print("Enviando uma notificação genérica...")

class Email(Notificacao):
    def enviar(self):
        # SOBREPOSIÇÃO: Mudamos o comportamento completamente
        print("Enviando e-mail: Verificando servidor SMTP e disparando...") # <- Sobrescreve enviar da pai(Notificacao)

class SMS(Notificacao):
    def enviar(self):
        print("Enviando SMS: Codificando para 160 caracteres...") # <- Sobrescreve enviar da pai(Email)

# Teste
notificacoes = [Notificacao(), Email(), SMS()]
for n in notificacoes:
    n.enviar() # Cada um executa sua própria versão
#
# ################################################################################################################
#
# 2. A Função super(): O Elo de Ligação
#
# O super() é um objeto temporário da superclasse que permite chamar métodos da classe pai de dentro da classe filha.
# Isso é vital quando você quer estender um comportamento em vez de substituí-lo completamente.
#
# No Construtor(__init__):
# Como vimos, é essencial para garantir que os atributos da base sejam inicializados corretamente.
#
# Em Métodos Comuns:
# Útil para adicionar "camadas" de lógica. Imagine um sistma de banco onde toda transação precisar ser logada.
#
class VideoPlayer:
    def reproduzir(self):
        print("'SUPER': Iniciando o fluxo de vídeo...")

class PlayerComLog(VideoPlayer):
    def reproduzir(self):
        # 1. Faz algo ANTES do comportamento original
        print("LOG: Usuário apertou o play.")

        # 2. Executa o comportamento original da classe Pai(Superclasse - VideoPlayer)
        super().reproduzir()

        # 3. Faz algo DEPOIS do comportamento original
        print("LOG: Vídeo está sendo reproduzido com sucesso.")

print(20 * "-")

print("\nUso do super() em métodos comuns:\n")
player = PlayerComLog()
player.reproduzir()
#
# ################################################################################################################
#
# 3. Sobreposição de Atributos(Data Shadowing)
#
# Embora menos comum, podemos também sobrepor atributos. Se a classe pai tem self.versão = 1.0 e a filha define
# self.versão = 2.0, a instância da filha usará o valor 2.0.
#
class Base:
    def __init__(self):
        self.versao = 1.0

class Derivada(Base):
    def __init__(self):
        super().__init__()  # Inicializa a versão da classe Base
        self.versao = 2.0   # SOBRESCREVE o atributo criado no super().__init__() <- vem da classe Base

print(20 * "-")
print("\nSobreposição de Atributos (Data Shadowing):\n")
obj = Derivada()
print(f"Versão da classe Derivada: {obj.versao}")  # Output: Versão da classe Derivada: 2.0
#
# ################################################################################################################
#
# 4. Por que usar super() em vez do nome da classe?
#
# Poderiamos chamar o pai usando Notificacao.enviar(self), mas o super() é superior por dois motivos:
#
# -> Indireção: Se você mudarmos o nome da classe pai, só precisa mudar na definição da classe filha(class Filha(NovoNomePai)),
# e o super() continuará funcionando.
#
# -> Herança Múltipla: O super() é inteligente o suficiente para seguir o MRO(Method Resolution Order) do Python, garantindo
# que cada classe na hierarquia seja chamada apenas uma vez.
#
# ################################################################################################################
#
# Resumo para o Roadmap
#
# -> Override: Use quando a classe filha precisar de uma lógica totalmente diferente da classe Pai.
#
# -> super(): Use quando a classe filha precisa da lógica da classe Pai mais algo extra, seja antes ou depois.
#
# -> Manutenibilidade: O uso de super() mantém o código resiliente a mudanças da árvore de classes.
#
# #################################################################################################################
#
# --- Fim --- 
#
# ################################################################################################################