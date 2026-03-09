# Prática: Polimorfismo, Assinatura de Métodos e LSP(Liskov Substitution Principle)
#
# #######################################################################################################
#
# Para consolidar a teoria, vamos aplicar o Polimorfismo e o LSP em um cenário real de Backend: um Sistema de Notificações.
#
# O objetivo é criar uma estrutura onde o motor principal do sistema não precise saber como uma mensagem é enviada, apenas 
# que ela pode ser enviada.
#
# #######################################################################################################
#
# 1. Definindo o Contrato(Classe Abstrata)
#
# Aqui estabelecemos a Assinatura do Método. Qualquer classe que herdar de Notificacao precisa ter um método enviar que aceite 
# exatamente um argumento: mensagem(msg).
#
# Exemplo:

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg):
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:
        """Assinatura: recebe nada (usa self.msg) e retorna bool"""
        pass

# #######################################################################################################
#
# 2. Implementando o Polimorfismo (Subclasses)
#
# Aqui, Email e SMS são formas diferentes (poli-morfismo) da mesma ideia.
#
# Exemplo:

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f"\nE-mail: Enviando '{self.msg}' via SMTP...")
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f"SMS: Enviando '{self.msg}' via Broker Mobile...")
        return True

# #######################################################################################################
#
# 3. O Motor Polimórfico
#
# Esta função é o coração da Engenharia de Software. Note que ela espera um objeto do tipo Notificacao. Ela não se 
# importa se é Email, SMS ou um futuro "WhatsApp".
#
# Exemplo:

def notificar_usuario(notificacao: Notificacao):
    # Polimorfismo: o Python decide em tempo de execução qual 'enviar' chamar
    status = notificacao.enviar()
    
    if status:
        print("✅ Sucesso no processamento.")
    else:
        print("❌ Falha no processamento.")

# #######################################################################################################
#
# 4. Aplicando o LSP (Liskov Substitution Principle)
#
# O LSP diz que a classe filha deve ser substituível pela pai sem quebrar o sistema.
#
# ** O erro comum(Violação do LSP) **: Criar uma classe NotificacaoPush que exige um parâmetro extra no método 
# enviar(self, token). Isso quebraria a função notificar_usuario, que só passa a mensagem no construtor e chama
# o método sem argumentos.
#
# Exemplo do erro:
#
# ❌ A Violação do LSP (O que NÃO fazer)
# Neste exemplo, a classe NotificacaoPush exige um token que a classe pai não previu. Isso impede que ela substitua 
# a classe pai de forma transparente.
#
# class Notificacao:
#    def enviar(self):
#        print("Enviando notificação genérica...")
#
# class Email(Notificacao):
#    def enviar(self):
#        print("Enviando e-mail: Olá, seu boleto chegou!")
#
# VIOLAÇÃO AQUI:
# class NotificacaoPush(Notificacao):
#    def enviar(self, token): # Mudou a assinatura (exige token)
#        print(f"Enviando Push para o token {token}")
#
# def processar_envio(notificacao: Notificacao):
#    # Esta função espera que qualquer 'Notificacao' funcione sem argumentos
#    notificacao.enviar()
#
# Isso funciona:
# processar_envio(Email()) 
#
# ISSO QUEBRA (TypeError): O programa "esperava" T, mas S exige algo a mais.
# processar_envio(NotificacaoPush())
#
# Atenção: O LSP diz que a classe filha deve ser substituível pela pai sem quebrar o sistema.
#
# ########################################################################################################
#
# ✅ A forma correta (Respeitando o LSP):
#
# Toda a configuração específica (token, número, e-mail) deve ser resolvida no __init__ ou internamente, mantendo
# a assinatura do método enviar idêntica à do pai.
#
# externo iterage com ela. Passamos as especificidades(como o token) no método construtor.
#
# Exemplo:
#

class NotificacaoPush(Notificacao):
    def __init__(self, msg, token):
        super().__init__(msg)
        self.token = token

    def enviar(self) -> bool:
        # Respeita a assinatura do pai: não pede o token aqui!
        print(f"Enviando Push para o token {self.token}: {self.msg}")
        return True
    
# --- TESTE FINAL ---
notificar_usuario(NotificacaoEmail("Olá, seu boleto vence hoje!"))
notificar_usuario(NotificacaoSMS("Seu código de acesso é 1234!"))
notificar_usuario(NotificacaoPush("Nova mensagem recebida","TOKEN_SECRETO_1234"))

#
# ########################################################################################################
#
# Resumo para o Roadmap
#
# - Polimorfismo: Permite que classes diferentes sejam tratadas de forma uniforme.
#
# - LSP: Garante que uma classe filha seja substituível pela classe pai sem quebrar o sistema.
#
# - Em sistemas de alto desempenho, o Polimorfismo permite que você carregue dinamicamente "drivers" ou "plugins".
#   Se você precisar de um novo tipo de log ou banco de dados, basta criar uma nova classe que respeite o contrato (LSP)
#   e sua aplicação principal nem sentirá a mudança.
#
# #########################################################################################################
#
# --- FIM ---
#
# #########################################################################################################