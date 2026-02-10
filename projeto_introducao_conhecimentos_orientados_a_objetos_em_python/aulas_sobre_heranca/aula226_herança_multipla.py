# Herança Mútipla - Python Orientado a Objetos
#
# ################################################################################################################
#
# 1. O que é Herança Múltipla?
#
# Ocorre quando uma Subclasse herda de duas ou mais Superclasses. Isso permite que o objeto "filho" combine 
# funcionalidades de diferentes "pais". No entanto, a herança múltipla pode levar a ambiguidades, especialmente quando 
# as superclasses possuem métodos com o mesmo nome.
#
# Sintaxe Básica:
#
print("\nHerança Múltipla em Python, Sintaxe Básica:\n")
class LogMixin:
    def log(self, msg):
        print(f"[LOG]: {msg}")

class Conexao:
    def conectar(self):
        print("Conectando ao servidor...")

# Herança Múltipla: Smartphone herda de A e B
class Smartphone(LogMixin, Conexao):
    pass

celular = Smartphone()
celular.log("Iniciando GPS") # Vem de LogMixin
celular.conectar()           # Vem de Conexao

# ################################################################################################################
#
# 2. O Problema do Diamante (Diamond Problem)
#
# O grande desafio da herança mútipla surge quando há uma ambiguidade na árvore de herança. Imagine a seguite estrutura:
#
# 1. A classe A define um método comum chamado quem_sou_eu().
#
# 2. As classes B e C herdam de A e cada uma altera(faz override) do método quem_sou_eu() para retornar uma string diferente.
#
# 3. A classe D herda de B e C ao mesmo tempo.
#
# Se cahmarmos o método d.quem_sou_eu(), qual versão o Python deve executar? A de B ou A de C?
#
# ##################################################################################################################
#
# 3. MRO: Method Resolution Order(A Solução)
#
# Para resolver o conflito acima, o Python utiliza um algoritmo chamado de C3 Linearization, para determinar a MRO
# (Ordem de Resolução de Métodos).
#
# A regra básica é: o Python busca o método da esquerda para a direita e de baixo para cima(da classe mais específica para
# a mais genérica).
#
# Consultando o MRO
#
# Podemos ver o comportamento do MRO usando o método mro() ou o atributo __mro__:
#

print(20 * "-", "\nExemplo do Problema do Diamante e MRO:\n")
class A:
    def info(self): print("Sou A")

class B(A):
    def info(self): print("Sou B")

class C(A):
    def info(self): print("Sou C")

class D(B, C):
    pass

print(D.mro()) # <- Saída em lista
# Saída: [D, B, C, A, object]
#
# print(D.__mro__) # <- Saída em tupla
#
# Neste caso, D().info() imprimirá "Sou B", porque B foi listado primeiro de D(B, C).
# print(D().info()) # Saída: "Sou B"
#
# ##################################################################################################################
#
# 4. Mixins: A Boa Prática da Engenharia de Software
#
# Na prática profissional, a herança mútipla e muito usada através de Mixins. Um Mixin é uma classe "pequena" que não
# foi feita para ser instanciada sozinha, mas apenas para fornecer uma funcionalidade extra a outras classes.
#
# Dica de Engenharia: Use herança mútipla preferencialmente para adicionar comportamentos(Mixins) e mantenha a hierarquia
# principal(a "natureza" do objeto) em uma herança simples.
#
# ###################################################################################################################
#
# 5. Resumo Técnico
#
# - Flexibilidade: Permite compor objetos complexos a partir de peças simples.
#
# - Ordem Importa: A ordem das classes dentro dos parênteses (B,C) define quem tem a prioridade no MRO.
#
# - super(): Em herança múltipla, o super() não chamar necessariamente o "pai direto", mas sim o próximo na lista do MRO.
#
# #####################################################################################################################
#
# --- FIM ---
#
# #####################################################################################################################