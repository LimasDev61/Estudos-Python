# Mixin e Abstração
#
# ################################################################################################################
#
# Enquanto o Mixin foca em compartilhar habilidades, a abstração foca em definir regras.
#
# #################################################################################################################
#
# 1. Mixins: Habilidades Adicionais
#
# Um Mixin é uma classe projetada para fornecer métodos a outras classes através da herança múltipla, mas que não deve
# se instanciada sozinha.
#
# Analogia: Imagine um video game. Voc}e tem a classe Guerreiro. O Mixin seria uma "habilidade" de Voar. Você não joga
# com o "Voar", mas sim com um Guerreiro que sabe Voar.
#
# Exemplo Prático: Mixin de Log
#

class LogMixin:
    def log(self, mensagem):
        print(f"[LOG: {self.__class__.__name__}]: {mensagem}")

class ConexaoDB(LogMixin):
    def conectar(self):
        self.log("Conectando ao banco de dados...")
        # Simula a conexão

class PrecessarPagamento(LogMixin):
    def processar(self):
        self.log("Processando pagamento...")
        # Simula o processamento

# Uso
print(20 * "-", "\nExemplo de Mixins para compartilhar habilidades de Log:\n")
con = ConexaoDB()

con.conectar() # Vem de LogMixin
pagamento = PrecessarPagamento()
pagamento.processar() # Vem de LogMixin

# ################################################################################################################
#
# 2. Abstração: O Contrato
#
# A Abstração(através de Classes Abastratas) é o processo de criar uma classe que serve apenas como um "molde obrigatório".
# Ela define o que deve ser feito, mas não como deve ser feito.
#
# Em Python, usamos o módulo "abc"(Abstract Base Classes).
#
# Por que usar?
#
# Para garantir que toda subclasse implemente métodos específicos. Se você tentar instanciar uma classe abstrata ou esquecer
# de criar um método obrigatório na filha, o Python lançará um erro.
#
# Exemplo:
#
from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        """Este método é obrigatório para todas as filhas(subclasses)."""
        pass

class Email(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando E-mail: {mensagem}")

class SMS(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

print("\n", 20 * "-", "\nExemplo de Abstração com Classes Abstratas:\n")
# teste = Notificacao() # ❌ ERRO: Não se pode instanciar classe abstrata
e = Email()
e.enviar("Olá, Renan!") # ✅ OK

s = SMS()
s.enviar("Olá, Renan!") # ✅ OK

# ################################################################################################################
#
# 3. Diferença Crucial: Mixins vs. Abstração
#
# Características            Mixins                                    Classes Abstratas(ABC)
# -------------------------|------------------------------------------|-----------------------------------------------------
# Objetivo                 | Adicionar Funcionalidades Extras.        | Definir uma interface/contrato comum.
# -------------------------|------------------------------------------|-----------------------------------------------------
# Herança                  | Usado em herança múltipla.               | Base da hierarquia("Pai").
# -------------------------|------------------------------------------|-----------------------------------------------------
# Instanciação             | Não deve ser instanciado diretamente.    | Não pode ser instanciado diretamente.
# -------------------------|------------------------------------------|-----------------------------------------------------
# Métodos                  | Geralmente tem métodos prontos.          | Geralmente tem métodos vazios (@abstractmethod).
# --------------------------------------------------------------------------------------------------------------------------
#
# #################################################################################################################
#
# 4. Resumo para o Roadmap
#
# - Use Mixins quando quiser que classes totalmente diferentes (ex: Usuario e Pedido) tenham a mesma funcionalidade 
# (ex: converter_para_json).
#
# - Use Abstração quando quiser criar uma base sólida para um sistema (ex: todos os MeiosDePagamento devem obrigatoriamente
#  ter o método validar()).
#
# #################################################################################################################
#
# --- FIM ---
#
# #################################################################################################################