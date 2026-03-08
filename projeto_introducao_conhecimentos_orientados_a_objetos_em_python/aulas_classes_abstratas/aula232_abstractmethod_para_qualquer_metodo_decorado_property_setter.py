# Abstractmethod para qualquer Método Decorado(property e setter)
#
# #############################################################################################################
#
# Essa é uma técnica avançada e extramamente útil na Engenharia de Software. Em Python, você pode combinar o 
# decorador @abstractmethod com outros decoradores, como o @property e @setter, para obrigar as subclasses a
# implementarem não apenas métodos comuns, mas também "atributos controlados".
#
# Isso garante que qualquer classe filha tenha obrigatoriamente aquela propriedade, mantendo consistência da 
# API do seu sistema.
#
# #############################################################################################################
#
# 1. Propriedades Abstratas(@property)
#
# Quando definimos uma @property como abstrata, podemos dizer: "Toda subclasse deve ter este atributo, e ele deve
# ser acessível como uma propriedade(sem parênteses)".
# 
# Exemplo:
#
from abc import ABC, abstractmethod

class Notificacao(ABC):
    @property
    @abstractmethod
    def remetente(self):
        """Toda notificação precisa ter um remetente"""
        pass

class Email(Notificacao):
    def __init__(self, endereco):
        self.endereco = endereco

    @property
    def remetente(self):
        # Implementação obrigatória da propriedade
        return f"E-mail enviado por: {self._endereco}"
        
# Se tentarmos criar uma classe que não implementa a property:
class SMS(Notificacao):
    pass

# # sms = SMS() # ❌ Erro: Can't instantiate abstract class SMS with abstract method remetente

# ##############################################################################################################
#
# 2. Setter Abstrato(@setter)
#
# Podemos também exigir que uma subclasse implemente a lógica de escrita(Setter). No entanto, a sintaxe muda um pouco:
# aplicamos o @abstraticmethod dentro do método setter.
#
# Exemplo:
#

class ContaBancaria(ABC):
    @property
    @abstractmethod
    def saldo(self):
        pass

    @saldo.setter
    @abstractmethod
    def saldo(self, valor):
        pass

class ContaCorrente(ContaBancaria):
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        # Implementação obrigatória da lógica de escrita
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = valor

# ##############################################################################################################
#
# 3. Mas por que isso é importante no Roadmap?
#
# 1. Contratos Rigorosos: Em sistemas de grande escala, garantir que todos os objetos sigam a mesma estrutura
#    evita erros de AttributeError em tempo de execução.
#
# 2. Padronização de APIs: Se criarmos um framework de Backend, podemos obrigar a que todos os "Modelos" tenham
#    uma propriedade @id e um @data_criacao, independentemente de como eles são salvos.
#
# 3. Segurança de Tipos: Ao definir propriedades abstratas, você sinaliza para as ferramentas de análise de código
#    (como o MyPy ou o IntelliSense do VS Code) que aquele atributo "existirá" em qualquer instância de uma subclasse.
#
# ##############################################################################################################
#
# 4. Resumo de Ordem dos Decoradores
#
# Sempre siga esta ordem para o Python interpretar os decoradores corretamente:
#
# -> Property Abstrata:
#    1. @property(em cima)
#    2. @abstractmethod(em baixo)
#
# -> Setter Abstrato:
#    1. @nome.setter(em cima)
#    2. @abstractmethod(em baixo)
#
# ##############################################################################################################
#
# --- FIM ---
#
# ##############################################################################################################