# Métodos de Classe(@classmethod) + Factories Methods(Métodos de Fábrica)
#
# #######################################################################################################
#
# Os métodos de classe(@classmethod) são ferramentas em arquitetura fundamentais na Engenharia de Software.
# Eles permitem que possamos criar comportamentos que pertencem a Classe, e não a um objeto específico.
#
# Enquanto o método comum usa o self(referência ao objeto/instância), o @classmethod usa o cls(referência
# à própria classe).
#
# #######################################################################################################
#
# 1. O que é o @classmethod?
#
# Um método de classe recebe a própria classe como primeiro argumento. Isso significa que ele tem acesso
# aos atributos da classe e pode ser chamado sem que você precise instanciar um objeto primeiro.
# 
# Exemplo:


print("\n1. Utilizando classmethod para alterar um atributo de classe:\n")
class Usuario:
    plataforma = "Web"

    @classmethod
    def alterar_plataforma(cls, nova_plataforma):
        cls.plataforma = nova_plataforma # Altera para todas as futuras instâncias e atuais.


print("Primeira impressão da plataforma: ", Usuario.plataforma) # <- Imprime: Web

mudar_plataforma = Usuario.alterar_plataforma # <- Armazena a função em uma variável
mudar_plataforma("Android\n") # <- Chama a função, alterando a plataforma

print("Segunda impressão da plataforma, alterado: ", Usuario.plataforma) # <- Imprime: Android, nova plataforma.

# #######################################################################################################
#
# 2. Factory Methods(Métodos de Fábrica)
#
# Este é o uso mais nobre e comum do @classmethod. Na Engenharia de Software, uma fábica é um padrão que
# ajuda projetos a criarem objetos de formas mais alternativas.
#
# -> O Problema: O método __init__ só pode ter uma assinatura. E se quisermos criar um usuário a partir de
# um dicionário JSON, ou a parti de uma data de nascimento?
#
# -> A Solução: Criar um Factory Method.
#
# Exemplo Prático: Backend de Cadastro de Usuários

from datetime import date

print(20 * "-")
print("\n2. Factory Methods(Métodos de Fábrica), para criar um usuário a partir de uma data de nascimento:\n")
class Usuarios:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_por_ano_nascimento(cls, nome, ano_nascimento):
        # Lógica Extra: Calcular a idade antes de criar o objeto
        idade = date.today().year - ano_nascimento

        # Retorna a própria classe instanciada(cls = Usuarios)
        return cls(nome, idade)
    
    # @classmethod
    # def criar_apartir_de_json(cls, json): <- Exemplo de JSON
    #     # Imagine que dados_json veio de uma API externa(dict)
    #     return cls(dados_json["nome"], dados_json["idade"])


# --- Execução ---

# 1. Forma Padrão:
user_1 = Usuarios("Renan Lima", 25)
print("Forma Padrão, sem Factory Method: ", user_1.nome, user_1.idade, "\n") # <- Imprime: Renan Lima 25

# 2. Forma com Factory Method:
user_2 = Usuarios.criar_por_ano_nascimento("Renan Lima", 1992)
print("Forma com Factory Method: ", user_2.nome, user_2.idade, "\n") # <- Imprime: Renan Lima 22

# 3. Usando a Fábrica JSON:
# user_3 = Usuarios.criar_apartir_de_json(dados_json) <- Exemplo de JSON
# print("Forma com Factory Method: ", user_3.nome, user_3.idade, "\n") # <- Imprime: Renan Lima 22

# ########################################################################################################
#
# 3. Por que usar cls(...) em vez de Usuario(...)?
#
# Dentro do @classmethod, usamos return cls(...). Isso é uma boa prática de engenharia devido a Herança.
#
# -> Se você criar a classe Admin que herda a classe Usuarios, o método de fábrica criar_por_ano_nascimento()
# funcionará corretamente para ambos os objetos, retornando um objeto Admin e não um Usuarios genérico.
#
# ########################################################################################################
#
# 4. Crucial Diferença de Instância vs. Classe
#
# Características            Métodos de Instância                       Métodos de Classe(@classmethod)
# -------------------------|------------------------------------------|-----------------------------------------------------
# Acesso                   | self(o objeto)                           | cls(a classe)
# Argumento                | atributos do objeto e da classe(self)    | Apenas atributo de classe(cls)
# Chamada                  | instancia.metodo()                       | Classe.metodo()
# Objetivo                 | Alterar o estado do objeto               | Criar novos objetos ou gerenciar a classe
# --------------------------------------------------------------------------------------------------------------------------
#
# ########################################################################################################
#
# -> Resumo para o Roadmap:
#
# 1. Use @classmethod sempre que precisar de construtores alternativos(métodos de fábrica).
#
# 2. Eles mantêm sua classe organizada: A lógica de "como transformar dados brutos em um objeto", fica dentro
# da prória classe.
#
# 3. Podemos carregar grandes volumes de dados(como um JSON massivo) e usar um @classmethod para distribuir esses
# dados em milhares de objetos de forma eficiente.
#
# ########################################################################################################
# 
# ---- FIM ------
#
# ########################################################################################################