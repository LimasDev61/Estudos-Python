# Atributos de Classe
#
# ###################################################################################################################
#
# Os ATRIBUTOS DE CLASSE são variáveis que pertencem à classe em si, e não a um objeto específico. Se você pensar
# na classe como um molde, o atributo de classe é uma característica gravada no próprio molde, enquanto os atributos
# de instância são detalhes que você pinta em cada peça depois de pronto. 
#
# ###################################################################################################################
#
# 1. Onde e como definir?
#
# Eles são definidos diretamente dentro da classe, mas fora de qualquer método(como o __init__).
#
# Exemplo:
#
separador = 20 * "-"
class Servidor:
    # Atributo de Classe
    # Todos os servidores da minha empresa usam o mesma localização.
    LOCALIZACAO = "São Paulo"
    prefixo_log = "[SISTEMA-BACKEND] - "
    contador = 0

    def __init__(self, ip):
        self.ip = ip

        # Acessando e alterando o contador de produção da classe.
        Servidor.contador += 1
#
# Acessando Servidor sem precisar criar um objeto
print("\nAcessando Servidor.LOCALIZACAO:", Servidor.LOCALIZACAO)
#
# ###################################################################################################################
#
# 2. Compartilhamento Total - Comportamento
#
# A característica mais importante é que, se você alter um atributo de classe, todos os objetos existentes(e os futuros)
# verão essa mudança instantaneamente.
#
# Exemplo:
#
s1 = Servidor("198.168.0.1")
s2 = Servidor("198.168.0.2")
#
# Alterando o valor do atributo da Classe
Servidor.LOCALIZACAO = "Brasília"
#
print("\nAcessando com nova localização Servidor.LOCALIZACAO:", Servidor.LOCALIZACAO)
print("Acessando s1.LOCALIZACAO:", s1.LOCALIZACAO)
print("Acessando s2.LOCALIZACAO:", s2.LOCALIZACAO)
print(f"\n{separador}")
#
# ###################################################################################################################
#
# 3. O Perigo da Sombra(shadowing)
#
# Este é um ponto crítico para um desenvolvedor de software. Se você tentar alterar um atributo de classe usando o 
# self, o Python não alterará o valor global. Em vez disso, ele criará um novo atributo de instância com o mesmo
# nome, "escondendo" o valor do atributo de classe apenas para o objeto em questão.
#
# Exemplo:
#
print("\nTudo abaixo vai ser sobre o erro do SHADOWING\n")
#
# Isso não muda o Servidor.LOCALIZACAO, mas cria uma instância de s1.LOCALIZACAO
s1.LOCALIZACAO = "Livepool"
#
print(f"Acessando s1.LOCALIZACAO: {s1.LOCALIZACAO} <- Shadowing, mudou apenas para S1") 
# Saída: Livepool <- Alterado apenas para o s1(Shadowing de Servidor.LOCALIZACAO)

print("Acessando Servidor.LOCALIZACAO:", Servidor.LOCALIZACAO) # Saída: Sao Paulo <- Não foi alterado
print("Acessando s2.LOCALIZACAO:", s2.LOCALIZACAO) # Saída: Sao Paulo <- Nao foi alterado
print(f"\n{separador}")
#
# obs: Sempre priporize acessar os atributos de classe, diretamente pela classe, e nunca pela instância, a não ser
# que precise verificar os dados dos atributos de classe para com o objeto.
#
# s1.LOCALIZACAO <- Incorreto, deve ser Servidor.LOCALIZACAO.
#
# ###################################################################################################################
#
# 4. Resumo Comparativo
#
# Característica           | Atributos de Instância              | Atributos de Classe
# -------------------------|-------------------------------------|------------------------
# Definição                | Dentro do método(usa-se self)       | Fora dos Métodos(usa-se classe)
# Escopo                   | Exclusivo de Objeto(Local)          | Exclusivo da Classe(Globais)
# Uso de Memória           | Multiplicado pelo Número de Objetos | Único na Memória(Econômico)
# Melhor para...           | Dados Únicos(ID, NOME, CPF)         | Constante, Configurações, Contadores
#
# ###################################################################################################################
#
# --> Exemplo de Engenharia: Contador de Instâncias
#
# Uma utilidade clássica é contar quantos objetos foram criados durante a execução do programa.
#
print("\nExemplo de Engenharia: Contador de Instâncias\n")
print("Contagem dos objetos criados de S1 + S2:", Servidor.contador)
print(f"\n{separador}")
#
# ###################################################################################################################
#
# --> Erro de Chamada, Exemplo:
#
# Se um atributo numérico de uma classe for alterado após a realização de cálculos ou da impressão inicial, qualquer 
# saída subsequente que dependa desse valor será inconsistente com o estado anterior.
#
# class Pessoa:
#     ano_atual = 2022 <- Atributo de Classe definido
#
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def get_ano_nascimento(self):
#         return Pessoa.ano_atual - self.idade <- O erro começa aqui
#
#
# p1 = Pessoa('João', 35) <- objeto definiu a idade 35, para subtrair de 2022, obtendo o resultado 1987
# p2 = Pessoa('Maria', 12) <- objeto definiu a idade 12, para subtrair de 2022, obtendo o resultado 2010
# print(Pessoa.ano_atual) 
#
# Segunda chamada com a alteração do atributo de classe, para um novo valor inconsistente
# Pessoa.ano_atual = 1 <- Atributo de Classe alterado
#
# print(p1.get_ano_nascimento()) <- com a nova definição, objeto com idade 35, para subtrair de 1, obtendo o resultado -34
# print(p2.get_ano_nascimento()) <- com a nova definição, objeto com idade 12, para subtrair de 1, obtendo o resultado -11
#
# Então nunca altere o atributo de classe, a menos que tenha uma razão clara para isso!
#
# ###################################################################################################################
#
# ------ FIM ------
#
# ##################################################################################################################