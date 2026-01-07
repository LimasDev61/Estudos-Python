# Entendendo o self em classes
#
# ###############################################################################################################
#
# -> O que é o self?
# 
# O self é uma um conceito criado por convenção para referenciar o objeto
# instânciado pela classe.
#
# ###############################################################################################################
# 
# 1. Analogia do "Cracha"
#
# Imagine que você está em um uma assistência técnica de clulares. Você tem uma pilha de 10 celulares na bancada.
# Todos eles vieram do mesmo projeto inicial(A Classe).
#
# Se você escrever um bilhete(cracha) dizendo - troque a bateria "deste" celular, a palavra "deste" se refere ao
# ao self do objeto instânciado pela classe na memória(heap).
#
# -> Se você pegar o celular A, "deste" refere-se ao celular A.
# -> Se voce pegar o celular B, "deste" refere-se ao celular B.
#
# Sem o self, o Python não saberá em qual dos 10 celulares ele deveria trocar a bateria.
#
# ###############################################################################################################
#
# 2. Por que ele é o primeiro Parâmetro?
#
# Diferente de linguagens como C# onde existe o "this" como palavra reservada e implícita,
# o Python optou por usar seu equivalente(self) dele de forma explicíta. No entanto, o self não
# é uma palavra reservada da linguagem Python - Ela poderia ter qualquer nome(até mesmo abacate).
# Mas por convenção o uso do self é recomendado fortemente pela comunidade Python.
#
# -> Exemplo:
#
# Quando nós definimos:
#
# def ligar(self):
#     self.ligado = True
#
# O Python faz algo automático por baixo dos panos. Quando você digita meu_celular.ligar(), o Python
# traduz isso para: Celular.ligar(meu_celular).
#
# Ou seja, ele passa o objeto como o primeiro argumento da função para que ela saiba em qual objeto ela se refere,
# e quais atributos ela deve modificar.
#
# ###############################################################################################################
#
# 3. O Self na Prática(Estado vs. Classe)
#
# Vamos ver como o self, diferência os dados de dois objetos criados a parti da mesma classe.

class Celular:
    # self.marca -> cria um atributo único para cada instância da classe.
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

        self.poweron = False # atributo padrão para todos os celular criado por essa classe para indicar
        # que ele comece desligado.

    def ligar(self):
        # O self busca o dado no objeto específico que chamou o método, para modificar o estado dele.
        self.poweron = True   

    def mostrar_info(self):
        # O self busca o dado no objeto específico que chamou o método, para mostrar suas informações.
        print(f"\nMarca: {self.marca}\nModelo: {self.modelo}\nPowerOn: {self.poweron}\n")


# Não faça isso:
#
# Celular.ligar() <- Não faça isso sem o objeto ser instânciado, pois a classe(molde) precisa do 
# objeto para que o self possa acessar seus dados.

# Instânciando os objetos da classe - Celular
celular_a = Celular("Samsung", "S10") # <- Instânciando o objeto celular_a da classe Celular
celular_b = Celular("Apple", "Iphone 12") # <- Instânciando o objeto celular_b da classe Celular

celular_a.mostrar_info() # <- Mostrando as informações do celular_a, através do self(self.marca, self.modelo, self.poweron)
celular_b.mostrar_info() # <- Mostrando as informações do celular_b, atraves do self(self.marca, self.modelo, self.poweron)

print(10*"-")
print("Celulares Ligados:")
celular_a.ligar() # <- Ligando o celular_a
celular_b.ligar() # <- Ligando o celular_b
celular_a.mostrar_info() # <- Informação atualizada com self.poweron = True
celular_b.mostrar_info() # <- Informação atualizada com self.poweron = True

# Quando instânciamos os objetos da classe, cada objeto vai ter um endereço de memória diferente.
# esse espaços dados armazenados dos objetos e persistem até sejam modificados ou o programa seja encerrado.
# O self é a essência para acessar esses espaços de memória:
#
# o celular_a, vai ser instânciado assim: <- novo endereço de memória criado
# self.marca = "Samsung" 
# self.modelo = "S10"
# self.poweron = False
#
# o celular_b, vai ser instânciado assim: <- novo endereço de memória criado
# self.marca = "Apple"
# self.modelo = "Iphone 12"
# self.poweron = False
#
# ##############################################################################################################
#
# 4. Onde o self é obrigatório?
#
# -> No __init__: Para caraimbar os dados iniciais do objeto.
#
# -> Nos métodos de instância: Para que o método consiga ler ou alterar outros atributos do objeto.
#
# -> Para chamar outros métodos: Se você quiser que um método chame outro dentro da mesma classe,
# pode se usar o self.outro_metodo(), como no exemplo abaixo:
#
# def metodo1(self):
#     self.metodo2()
#
# def metodo2(self):
#     print("Oi") 
#     
# O self permite que o Python entenda que o self.metodo2() se refere ao self.metodo2() da classe.
#
# ###############################################################################################################
#
# 5. Resumo Engenharia de Software
#
# Termo                | Função do self
# ---------------------|-------------------------------------------------------
# Escopo               | Define que a variável pertence ao objeto, não função local.
# Indentidade          | Garante que o objeto_1.nome, seja diferente do objeto_2.nome.
# Persistência         | Permite que os dados sobrevivam entre diferentes chamadas de métodos. 
#
# ###############################################################################################################
#
# 6. Resumo sobre Construção da Classe
#
# Termo                | Descrição
# ---------------------|-------------------------------------------------------
# Classe               | É um molde que geralmente não possui dados, verbos(metodos) e substantivos(atributos).
# Instância            | Tem os dados do objeto e seus verbos e substantivos referênciados pelo self.
# Uma Classe           | Pode gerar várias instâncias de objetos.
# O Self na Classe     | É a própria instância da classe.
#
# ###############################################################################################################
#
# --> Dica de Ouros: Se você esquecer o self na definição de um método(ex: def ligar_celular(..., senha ):), o
# Python apresentará uma mensagem de erro de TypeError dizendo que a função recebeu um argumento mas você não 
# definiu nenhum parâmetro para ele. Isso acontece porque o Python sempre tenta passar a instância da classe
# automaticamente como o primeiro argumento da função.
#
# ###############################################################################################################
#
# ------ FIM ------
#
# ###############################################################################################################