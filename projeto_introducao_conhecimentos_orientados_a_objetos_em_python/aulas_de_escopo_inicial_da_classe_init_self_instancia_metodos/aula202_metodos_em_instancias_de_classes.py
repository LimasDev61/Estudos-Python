# Métodos em Instâncias de Classes
#
# #######################################################################################################
#
# Os métodos são ações ou habilidades que o seus objetos possuem. Se os atributos são os substantivos(características),
# os métodos são os verbos(ações/comportamentos).
#
# Podemos pensar nos métodos como a interface de comunicação com o objeto: em vez de alterar os dados do objeto
# diretamente, podemos chamar um método para que o objeto altere a si próprio.
#
# ########################################################################################################
#
# 1. O que define um Método de Instância?
# 
# Um método de instância é uma função definida dentro de uma classe que:
# 
# -> Pode acessar e modificar os atributos do objeto.
# -> Sempre recebe o self como primeiro parâmetro.
# -> É chamado através de uma instância(ex: objeto.metodo()).
# 
# ########################################################################################################
# 
# 2. Exemplo Prático: Processador de Dados
# 
# Dado ao meu interesse em Data Science, vamos criar um exemplo de uma classe que processa uma lista de números.
# 
class AnalisarDados:
    def __init__(self, nome_projeto, numeros):
        self.nome_projeto = nome_projeto
        self.numeros = numeros # Atributo(Estado)

    # Método de Instância: Realiza uma ação utilizando os dados do objeto
    def calcular_media(self):
        if not self.numeros:
            return 0
        
        media = sum(self.numeros) / len(self.numeros)
        return media
    
    # Método que altera o estado do objeto
    def adicionar_dado(self, novo_numero):
        self.numeros.append(novo_numero)
        print(f"Número {novo_numero} adicionado ao projeto {self.nome_projeto}.")


# Uso:
projeto = AnalisarDados("Análise de Vendas", [100, 200, 300, 400])

# Chamando o método para calcular a média
print(f"Média Inicial: {projeto.calcular_media()}")  # Saída: Média Inicial: 250.0

# Chamando o método para adicionar um novo dado
projeto.adicionar_dado(500)

# Chamando o método para calcular a média novamente
print(f"Média Atualizada: {projeto.calcular_media()}")  # Saída: Média Atualizada: 375.0



# ########################################################################################################
#
# 3. Métodos chamando outros Métodos
#
# Uma das bases da engenharia de software é decomposição. Você pode criar métodos pequenos que são chamados
# por um método principal dentro da mesma classe. Para isso, usamos o self.nome_metodo().
# 
# Exemplo:
#
# class Relatorio:
#     def __init__(self, titulo, dados):
#         self.titulo = titulo
#         self.dados = dados
#
#     def _formatar_cabecalho(self):
#         return f"{self.titulo.upper()}\n" + "=" * len(self.titulo)
#     
#     def _formatar_corpo(self):
#        return return f"Conteúdo: {self.dados}"
# 
#     def gerar_relatorio_completo(self):
#        cabecalho = self._formatar_cabecalho()
#        corpo = self._formatar_corpo()
#        return f"{cabecalho}\n{corpo}"
# 
# ---> Nota de Engenharia: O uso do underline (_) antes do nome do método(ex: _formatar_cabecalho) é uma convenção
# em Python para indicar que o método é interno(protegido) e não deve sr chamado fora da classe
#
# ########################################################################################################
#
# 4. Por que usar Métodos em vez de Funções Externas?
#
# -> Encapsulamento: A lógica de como calcular a média de um AnalisarDados fica guardado dentro da classe.
# Se a fórmula mudar, você só altera em um lugar(classe/método).
# -> Organização: Seu código para de ser uma lista gigante de funções e passa a ser um conjunto de entidades
# (classes) com responsabilidades claras - que sabem o que fazem.
# -> Facilidade de Manutenção: Como os métodos estão vinculados ao self, eles têm acesso direto a todos os 
# atributos sem que você precise passar dez argumentos para cada função.
#
# ---> Resumo para meu RoadMap:
#
# -> Atributos: Guardam o estado(o que é objeto é)
# -> Métodos: Definem o comportamento(o que o objeto faz)
# -> self: É a ponte que permite ao método encontrar os atributos e outros métodos daquela instância específica.
#
# ##################################################################################################################
#
# ------ FIM ------
#
# ##################################################################################################################