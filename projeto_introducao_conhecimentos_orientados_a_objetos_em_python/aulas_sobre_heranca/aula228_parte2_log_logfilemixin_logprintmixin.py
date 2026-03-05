from abc import ABC, abstractmethod
import pathlib
# Log, LogFileMixin e LogPrintMixin
#
# ##################################################################################################################
#
# Para fechar o conceito de Mixins com uma aplicação real de Engenharia de Software, vamos construir um sistema de Log 
# flexível. Esse padrão é muito comum em grandes sistemas onde você deseja alternar entre salvar logs em arquivos, imprimir
# no console ou enviar para uma base de dados, sem mudar o código das suas classes principais.
#
# Aqui, o objetivo é criar "habilidades de log" que podem ser "plugadas" em qualquer classe.
#
# ##################################################################################################################
#
# 1. A Base: Classe Log(Abstração)
#
# Primeiro, definimos uma classe base. Embora não seja estritamente necessário para um Mixin, na Engenharia de Software,
# usamos uma classe abstrata para garantir que todos os Mixins de log sigam a mesma assinatura de método.
#
# Exemplo:

class Log(ABC):
    @abstractmethod
    def _log(self, mensagem):
        """Método interno que cada Mixin implementará à sua maneira"""
        pass

    def log_error(self, msg):
        return self._log(f"ERROR: {msg}")
    
    def log_success(self, msg):
        return self._log(f"SUCCESS: {msg}")
    
# ###################################################################################################################
#
# 2. Os Mixins: LogPrintMixin e LogFileMixin
#
# Agora criamos as implementações específicas. Note que elas herdam de Log, mas sua função é apenas fornecer a implementação
# do método _log.
#
# Exemplo:
#

# Caminho para o arquivo de log (usando sua máquina-desenvolvimento)
LOG_FILE_PATH = pathlib.Path(__file__).parent / "log_aula228.txt"

class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} (no arquivo: {LOG_FILE_PATH.name})\n"
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(msg_formatada + "\n")

# ###################################################################################################################
#
# 3. Aplicando na Prática(Composição via Herança)
#
# Imagine que temos uma classe Eletronico. Podemos decidir, no momento da criação da classe, qual a estratégia de log
# ela usará.
#
# Exemplo:

class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            # Se a classe herdar de um LogMixin, este método existirá.
            self.log_success(f"{self.nome} ligado com sucesso!")

# Especialização com Mixin de Console
class Smartphone(Eletronico, LogPrintMixin):
    pass


# Especialização com Mixin de Arquivo
class Tablet(Eletronico, LogFileMixin):
    pass

# --- Teste ---

print("Testando Smartphone com LogPrintMixin:")
smartphone = Smartphone("iPhone 15")
smartphone.ligar() # Saída no console: "SUCCESS: iPhone 15 ligado com sucesso!"

print("\nTestando Tablet com LogFileMixin:")
print(f"Verifique o arquivo {LOG_FILE_PATH} para a mensagem de log.")
tablet = Tablet("iPad Pro")
tablet.ligar() # Salva silenciosamente no arquivo log.txt: "SUCCESS: iPad Pro ligado com sucesso! (no arquivo: log.txt)"

# ###################################################################################################################
#
# 4. Por que isso é importante para o ROADMAP?
#
#   1. Flexibilidade Total: Se amanhã você precisar de um LogDatabaseMixin, você cria a classe e apenas muda a herança das 
#      suas classes principais(Eletronico).
#
#   2. Princípio da Responsabilidade Única (SRP): A classe Eletronico cuida da lógica do aparelho, enquanto o Mixin cuida 
#      exclusivamente da lógica de log.
#
#   3. Ambiente de Desenvolvimento: Em sua máquina de desenvolvimento, você pode manter logs detalhados em memória ou arquivo 
#      durante o desenvolvimento e trocar para um serviço de nuvem em produção apenas alterando o Mixin.
#
# ####################################################################################################################
#
# Resumo Técnico:
#
# - Log (ABC): Garante que o método log_error e log_success existam e chamem o _log.
#
# - LogPrintMixin: Implementa o _log enviando para a tela.
#
# - LogFileMixin: Implementa o _log persistindo no disco rígido.
#
# - Herança Múltipla: Permite que Smartphone seja um Eletronico e tenha a habilidade de Log.
#   permite que Tablet seja um Eletronico e tenha a habilidade de Log.
#
# #######################################################################################################################
#
# --- FIM ---
#
# # #####################################################################################################################