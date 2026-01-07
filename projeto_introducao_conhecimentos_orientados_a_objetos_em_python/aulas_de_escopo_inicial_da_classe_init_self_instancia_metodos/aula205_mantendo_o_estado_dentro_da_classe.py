# Mantendo o Estado Dentro da Classe
#
# ###################################################################################################################
#
# Manter o estado é o que diferência um objeto de uma simples função. Enquanto uma função "esquece" tudo o que fez
# assim que retorna um valor, um objeto "lembra" de suas informações durante toda a sua existência na memória.
#
# Na Engenharia de Software, o estado é o conjunto de valores armazenados nos atributos de instância de uma classe
# em um determinado momento.
#
# ###################################################################################################################
#
# 1. Como o Estado é Mantido?
#
# O estado é mantido através do parâmetro self. Quando você atribui um valor a self.nome_da_variavel, estamos
# reservando um espaço na memória RAM que ficará exclusivamente vínculado àquela instância da classe.
#
# ###################################################################################################################
#
# 2. Exemplo Prático: Um Pipeline de Dados
#
# Com o foco em ciências de dados e backend, vamos imaginar uma classe que gerência o estado de um processamento de
# dados.
#
# Exemplo:
#
class ProcessadorDeDados:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        
        # Estado Inícial
        self.dados = []
        self.status = 'Iniciado'
        self.processado = False

    def carregar_dados(self):
        # Alterando o estado interno
        self.dados = [10, 20, 30]
        self.status = 'Dados Carregados'
        print(f"Estado: {self.status}.")

    def aplicar_filtro(self, limite):
        # O objeto "lembra" dos dados carregados no método anterior(carregar_dados)
        self.dados = [d for d in self.dados if d > limite]
        self.status = 'Dados Filtrados'
        print(f"Estado: {self.status}\nDados Atuais: {self.dados}")

    def finalizar_processamento(self):
        self.processado = True
        self.status = 'Finalizado'
        print(f"Estado final: {self.status}")
        return


# Uso do objeto mantendo o estado
pipeline = ProcessadorDeDados("Vendas.csv")

pipeline.carregar_dados() # Estado: Dados Carregados
pipeline.aplicar_filtro(20) # Estado: Dados Filtrados
pipeline.finalizar_processamento() # Estado final: Finalizado

#
# ###################################################################################################################
#
# 3. A Importância da Persistência de Estado
#
# Endender o "estado" é vítal por três motivos:
#
#  1. Contexto: O método aplicar_filtro() não precisou receber a lista de dados como argumento, porque a lista já
#   faz para do mundo do objeto.
#
#  2. Rastreabilidade: Podemos consultar pipeline.status a qualquer momento para saber em que fase o processo está.
#
#  3. Segurança de Thread: Em sistemas complexos, manter o estado isolado dentro de uma instância de classe
#   evita que um processo sobrevescrava os dados de outro(o que aconteceria se utilizassemos variáveis globais).
#
# ###################################################################################################################
#
# 4. Atributos de Classe vs. Atributos de Instância
#
# Tipo de Estado      | Onde Reside                          | Quem Enxerga?
# --------------------|--------------------------------------|---------------------------------
# Instância(self.x)   | Na memória individual de cada objeto | Apenas aquele objeto específico.
# Classe(x = ...)     | No molde da classe                   | Todos os objetos daquela classe(se um muda, todos mudam).
#
# ###################################################################################################################
#
# --> Nota de Engenharia: Evite manter estados importantes em atributos de classe, a menoss que seja algo 
# propopositalmente compartilhado(como uma config, contadores, etc).
#
# --> Resumo: Manter o estado permite que você crie sistemas complexos onde objetos conversam entre si.
# Um objeto "pedido" mantém o estado de pago ou enviado, enquanto um objeto "carrinho" mantém a lista de itens
# que o usuário escolheu.
#
# ##################################################################################################################
#
# ------ FIM ------
#
# ##################################################################################################################