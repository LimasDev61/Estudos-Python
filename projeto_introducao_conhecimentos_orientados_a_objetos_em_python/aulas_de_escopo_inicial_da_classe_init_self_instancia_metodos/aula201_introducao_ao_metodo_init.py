# Introdução ao método __init__(Inicializador de Atributos)
#
# O método __init__ é o que chamamos de Método Mágico(Dunder Method, por causa do duplo underscore).
# Ele é, essencialmente, a primeira coisa que acontece na vida de um objeto quando ele é criado.
#
# Pense nele como um contrato de nascimento do objeto: ele define quais dados são obrigatórios para que
# o objeto possa existir na memória.
#
# ###############################################################################################################
#
# 1. Qual é função real do __init__?
#
# Diferente do que muitos pensam, o __init__ não é um construtor de objetos.
# O verdadeiro construtor é o método __new__, que é responsável por alocar espaço na memória para o novo objeto.
# O __init__, por outro lado, é chamado logo após a criação do objeto para inicializar seus atributos.
#
# Resumindo, o __init__ é um inicilizador de atributos, usado para configurar o estado inicial do objeto, garantindo que ele 
# comece sua vida com todos os dados necessários, inicializados corretamente.
#
# ################################################################################################################
#
# 2. Características do obrigatórias do Método __init__
#
# -> Chamada Automática: Você nunca escreve user.__init__(). O Python faz isso sozinho quando você utiliza os 
# parênteses para criar uma nova instância da classe.
#
# -> O self é obrigatório: Ele deve ser o primeiro parâmetro do método __init__. Sem ele, você não conseguirá
# acessar os dados do objeto.
#
# -> Não possui return: O __init__ não deve retornar nada(ele sempre retorna None implicitamente). Sua única 
# missão é configurar o objeto.
#
# ################################################################################################################
#
# 3. Valores Padrão no Inicilizador(__init__)
#
# Como vimos nos estudos de funções, também podemos usar valores padrão nos parâmetros do __init__. Isso é muito
# útil para evitar que o usuário precise fornecer todos os dados ao criar um objeto ou configurações opcionais.
#
# Exemplo:
# class BancoDeDados:
#     def __init__(self, host="localhost", port=3306):
#         self.host = host
#         self.port = port
#
# #################################################################################################################
#
# 4. Resumo de Engenharia
#
# Característica               | Descrição
# -----------------------------|--------------------------------------------------------------
# Momento de Chamada           | O __init__ é chamado automaticamente após a criação do objeto.
# Parâmetros                   | Define o que é necessário para construir o objeto.
# Atributos                    | Transforma argumentos em dados persistentes no objeto via self.
# Importância                  | Garente que o bojeto não comece com dados vazios ou inconsistentes.
#
# ##################################################################################################################
#
# 5. Exemplo Prático do Método __init__ - Sistema de Cadastro
#
# Imagine que estamos criando um backend para uma plataforma. Todo usuario precisa de um nome e um email para se 
# cadastrar.
#
# obs: Vou utilizar keyword-only arguments para forçar o uso de nomes nos parâmetros do objeto.

class Usuario:
    def __init__(self,*, nome, email):
        self.nome = nome
        self.email = email
        self.logado = False  # Atributo padrão para todos os usuários, indicando que eles começam deslogados.
        print(f"Usuário {self.nome} criado com email {self.email}.")

# O momento em que o inicializador __init__ é chamado automaticamente:
user_1 = Usuario(nome = "Renan Lima", email = "renanalima@com")
user_2 = Usuario(nome = "Maria Silva", email = "mariasilva@com")

print(user_1.nome)  # Acessando o atributo nome do user_1
print(user_2.email) # Acessando o atributo email do user_2

# Mas o que aconteceu nos bastidores?
#
# 1. Você chamou o Usuario(...);
# 2. O Python criou um objeto vazio na memória;
# 3. Ele passou esse objeto vazio para o primeiro parâmetro do __init__(o self);
# 4. Ele passou "Renan Lima" para o parâmetro nome e "renanalima@com" para o email;
# 5. O self.nome = nome criou o atributo nome no objeto e atribuiu o valor "Renan Lima";
# 6. O self.email = email criou o atributo email no objeto e atribuiu o valor "renanalima@com";
# 7. O self.logado = False criou o atributo logado no objeto e atribuiu o valor False;
# 8. O __init__ terminou sua execução e retornou None implicitamente;
# 9. A variável user_1 agora referencia o objeto que foi criado e inicializado.
# Todo esse processo aconteceu automaticamente quando você criou a instância da classe Usuario.
#
# ###################################################################################################################
#
# Só um detalhe importante, kwargs funciona normalmente no __init__
#
# class Usuario:
    # def __init__(self,**kwargs):
    #     self.nome = kwargs.get("nome")
    #     self.email = kwargs.get("email")
    #     self.logado = False  # Atributo padrão para todos os usuários, indicando que eles começam deslogados.
    #     print(f"Usuário {self.nome} criado com email {self.email}.")
#
# ##################################################################################################################
#
# ------ FIM ------
#
# ##################################################################################################################