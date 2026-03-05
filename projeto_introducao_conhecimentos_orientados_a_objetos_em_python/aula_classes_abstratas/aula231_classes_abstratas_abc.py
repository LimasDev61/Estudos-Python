from abc import ABC, abstractmethod
# Classes Abstratas - Abstract Base Classes (ABC)
#
# ###################################################################################################################
#
# As Classes Abstratas(ou ABCs) são o pilar da abstração na Engenharia de Software. Elas funcionam como um contrato
# rigoroso: uma classe abstrata define o que as suas subclasses devem fazer, mas não necessariamente como elas devem
# fazer.
#
# Diferente da herança comum, você não pode criar um objeto diretamente de uma classe abstrata. Ela serve exclusivamente
# para ser herdada.
#
# ###################################################################################################################
#
# 1. Mas por que usar ABCs?
#
# Em muitos casos quando trabalhamos com herança, podemos encontrar situações onde é preciso de uma base comum para várias 
# funcionalidades, mas essa base, por si só, é incompleta.
#
# - Exemplo: Todo MeioDePagamento deve ter um método processar(). Mas não existe um objeto "MeioDePagamento" genérico no mundo
#   real; existem apenas Pix, Cartao, Boleto e assim por diante. 
#
# ###################################################################################################################
#
# 2. Criando uma ABC em Python
#
# Para criar uma classe abstrata, você precisa importar o módulo abc(Abstract Base Classes).
#
# Exemplo:

# Ao herdar de ABC, esta classe tora-se abstrata, ou seja, não pode ser instanciada diretamente, mas pode ser herdada como suporte
# para outras classes.
class MeioDePagamento(ABC):

    @abstractmethod
    def _processar(self, valor=None):
        pass

    def confirmar_pagamento(self, valor=None):
        if self._processar(valor):
            print("Pagamento aprovado\n")
        else:
            print("Pagamento recusado\n")


# ###################################################################################################################
#
# 3. A Obrigatoriedade de Implementação
#
# Se tentarmos criar uma subclasse e esquecer de implementar o @abstractmethod, o Python impedirá a criação do objeto.
#
# Exemplo:
#

class Pix(MeioDePagamento):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix

    def _processar(self, valor = None):

        if valor:
            print(f"Processando o pagamento com Pix no valor de {valor:,.2f} ")
            return True
        
        return False
    

class Cartao(MeioDePagamento):
    def __init__(self, numero, cvv, validade):
        self.numero = numero
        self.cvv = cvv
        self.validade = validade

    def _processar(self, valor = None):

        if valor:
            print(f"Processando o pagamento com Cartão de Crédito no valor de {valor:,.2f}")
            return True
        
        return False
    
# --- Teste de Instanciação ---

# n = MeioDePagamento() # ERRO TypeError: Can't instantiate abstract class MeioDePagamento with abstract methods _processar <- Erro

p = Pix("chave_pix")
p.confirmar_pagamento()

c = Cartao("1234", "123", "12/2022")
c.confirmar_pagamento(100)

# ###################################################################################################################
#
# 4. ABCs vs Interfaces
#
# Em linguagens como Java ou C#, existe a palavra-chave "interface". No Python, usamos as ABCs para o mesmo propósito.
#
# - Se uma classe abstrata tem apenas métodos abstratos, ela funciona como uma Interface.
#
# - Se ela tem métodos abstratos e métodos prontos(concretos), ela é uma Classe Abstrata clássica.
#
# ###################################################################################################################
#
# 5. Resumo de Engenharia de Software
#
# Recurso          | Descrição
# -----------------|-------------------------------------------------------------------------------
# ABC              | Classe base que sinaliza ao Python que esta é uma classe abstrata.
# -----------------|-------------------------------------------------------------------------------
# @abstractmethod  | Decorador que marca os métodos que as filhas devem obrigatoriamente criar.
# -----------------|-------------------------------------------------------------------------------
# Segurança        | Garante que o desenvolvedor não esqueça partes vitais do código.
# -----------------|-------------------------------------------------------------------------------
# Polimorfismo     | Permite tratar Pix e Cartao apenas como MeioDePagamento, sabendo que ambos têm o método _processar().
# -------------------------------------------------------------------------------------------------
# 
# ###################################################################################################################
#
# --- FIM ---
#
# ###################################################################################################################