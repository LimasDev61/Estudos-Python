# Escopo da Classe e de Metodos da Classe
# 
# ###################################################################################################################
#
# Compreender a diferença entre o Escopo de Classe, Escopo de Instância e o Escopo de Metodos da Classe é 
# fundamental para evitar um dos erros mais comuns na Engenharia de Software: a alteração acidental de dados globais
# quando você pretendia alterar apenas o objeto.
#
# Vamos ver a hierarquia de escopos de uma classe:
#
# ##################################################################################################################
#
# 1. Escopo de Classe(Atributos de Classe)
#
# Variáveis definidas diretamente dentro da classe, mas fora de qualquer método, pertecem ao escopo da classe.
# 
# -> Compartilhamento: Todos os objetos criados a parti desssa classe compartilham os mesmos dados(atributos valor)
#
# -> Uso Comum: Constantes, configurações padrão ou contadores de instâncias.
#
# ##################################################################################################################
#
# 2. Escopo de Instância(Atributos de Instância)
#
# Variáveis criadas dentro de métodos(geralmente no __init__) usando o prefixo self, pertencem ao escopo de instância.
#
# -> Isolamento: Cada objeto tem sua própria cópia desses dados. Alterar em um, não afeta os outros.
#
# # ##################################################################################################################
#
# 3. Escopo Local do Método(Variáveis de Bloco)
#
# Variáveis criadas dentro de um método sem prefixo self, pertencem ao escopo local do método.
# 
# -> Vida Útil: Elas nascem quando o método é chamado e morrem assim que o método termina. Elas
# não ficam salvas no objeto.
#
# ##################################################################################################################
#
# Exemplo Prático: Sistema de Fábrica
#
# Imagine que estamos modelando uma linha de produção.

class Celular:
    # 1. Escopo de Classe: Compartilhado por todos os celulares produzidos pela linha.
    FABRICANTE = "Minha_Marca" # <- Constante de Classe
    contador_producao = 0 # <- Contador de Instâncias

    print()
    def __init__(self, modelo):
        # 2. Escopo de Instância: Uníco para cada celular produzido pela linha.
        self.modelo = modelo # <- Atributo de Instância

        # Acessando e alterando o contador de produção da classe.
        Celular.contador_producao += 1

        # Posso usar uma variável sem self para mostrar que o método foi criado.
        variavel = f"Instância {self.modelo} criada com sucesso."
        print(variavel) # <- cada objeto(instância) tem sua cópia dessa variável.

    def consertar(self, peca):
        # Escopo Local de Método: A variável "custo" so existe dentro deste método.
        taxa_servico = 50.0
        custo = taxa_servico + 100.0 # Lógica temporária de negócio

        print(f"Consertando o celular {self.modelo}, a peça usada foi {peca} e o custo do reparo foi R$ {custo:.2f}.")
        # Ao sair desse método o custo e peca desaparecem da memória ram.

# Criando as Instâncias(Objetos) da Classe
celular_1 = Celular("Iphone X")
celular_2 = Celular("Iphone 11")

# Acessando os Atributos de Classe
print("\nAtributos de Classe:")
print(f"Fabricante: {Celular.FABRICANTE}")
print(f"Contador de Produção: {Celular.contador_producao}")

# Acessando os Atributos de Instâncias
print("\nAtributos de Instâncias:")
print(f"Modelo: {celular_1.modelo}")
print(f"Modelo: {celular_2.modelo}")

# Chamando o Escopo local do Método, dentro do Método de Instância(objeto) - Morre ao sair do Método.
print("\nChamando o Método de Instância:")
celular_1.consertar("Tela")

# ##################################################################################################################
#
# --> Comparação de Escopos
#
# Nivel de Escopo         | Onde é Definido?           | Como Acessar?              | Quanto tempo dura?
# ------------------------|----------------------------|----------------------------|---------------------
# Classe                  | Fora dos Métodos           | class.var ou self.var      | Equanto o programa rodar.
# Instância               | Dentro do __init__         | self.var                   | Equanto o objeto existir.
# Local do Método         | Dentro do Método           | objeto.metodo()            | Apenas durante a execução do método.
# 
# ##################################################################################################################
# 
# --> PERIGO! A Sombra(shadowing)
# 
# Um erro clássico é tentar alterar um atributo de classe usando self.
# 
# -> Se você fizer self.FABRICANTE = "Nova Marca", o Python não altera o valor para todos os objetos(celulares) criados.
# Em vez disso, ele cria um novo atributo de instância com o mesmo nome, "escondendo" o valor do atributo de classe
# apenas para o objeto em questão.
#
# Exemplo:
#
# celular_1.FABRICANTE = "Nova Marca" <- self.FABRICANTE incorreto.
#
# print(celular_1.FABRICANTE) # "Nova Marca" <- alterado apenas para o celular_1
# print(celular_2.FABRICANTE) # "Minha_Marca" <- Nao foi alterado
#
# ##################################################################################################################
#
# --> Mas o que aconteceu por de baixo dos Panos?
#
# 1. O Estado Inical: O Python olha para a classe e vê FABRICANTE = "Minha_Marca". Quando você pede 
# celular_1.FABRICANTE, ele não acha na instância, então sobe(um nível) para a classe e vê FABRICANTE = "Minha_Marca".
#
# 2. O Shadowing: Quando você faz celular_1.FABRICANTE = "Nova Marca", o Python cria uma nova entrada no 
# dicionário interno(__dict__) da instância celular_1, mas apenas para esse objeto em questão.
#
# 3. O Estado Final: Agora sempre que você pedir celular_1.FABRICANTE, ele vai olhar para o dicionário
# interno e encontrar "Nova Marca" na sua instância, e parará de procurar o valor FABRICANTE da classe,
# que nesse caso é "Minha_Marca"(ficou na sombra).
# 
# ##################################################################################################################
#
# --> Como evitar e fazer do jeito Correto?
#
# Se o seu bojetivo é mudar o fabrincante para todos os celulares de uma vez(mudar o valor do atributo de classe),
# devemos acessar diretamente o atributo pela classe.
#
# Exemplo:
#
# Celular.FABRICANTE = "Nova Marca"
# print(celular_1.FABRICANTE) # "Nova Marca"
# print(celular_2.FABRICANTE) # "Nova Marca"
#
# Agora sim alterou para todos, sem shadowing.
#
# ##################################################################################################################
#
# ------ FIM ------
#
# ##################################################################################################################