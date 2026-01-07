# __dict__ e vars() para Atributos de Instância
#
# #################################################################################################################
#
# Para um Engenheiro de Software, entender o __dict__ e a função vars() é como abrir o capô de um carro para como o
# motor está montado. Em Python, quase tudo o que vimos até agora sobre manter estado acontece dentro de um dicionário
# oculto.
#
# Aqui está como o Python armazena dados definidos via self.
#
# #################################################################################################################
#
# 1. O que é o __dict__?
#
# O __dict__ é um atributo especial(dunder method) que todo objeto Python possui por padrão. Ele é um dicionário que
# armazena todos os atributos de instância que você criou.
#
# -> Chave: O nome do atributo(string)
# -> Valor: O valor que atribuimos ao atributo.
#
# Exemplo:
#

separador = 20 * "-"
class Usuario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

user_1 = Usuario("Renan Lima", "Desenvolvedor")

print("\nImprimindo com __dict__ e vars():")
# Olhando por de baixo do capô:
print(f"\nUso do user_1.__dict__: {user_1.__dict__}") # Saída: {'nome': 'Renan Lima', 'cargo': 'Desenvolvedor'}
#
# #################################################################################################################
#
# 2. A Função vars()
#
# A função vars() é uma forma mais elegante(Pythonic) de acessar o __dict__.
#
# -> Se você passar o objeto para vars(objeto), ele retorna o __dict__ desse objeto.
# -> Se você chamar vars() sem argumentos, ele se comporta como locals(), mostrando as variáveis do escopo atual.
#
# Exemplo:
#
# Exatamente a mesma coisa que o user_1.__dict__
dados_usuario = vars(user_1)
print(f"\nUso do vars(user_1): {dados_usuario}") # Saída: {'nome': 'Renan Lima', 'cargo': 'Desenvolvedor'}
#
# Posso pegar esses dados separados:
print(f"\nPegando apenas um atributo do dicinário user_1: {dados_usuario['nome']}\n")# Saída: Renan Lima
print(separador)
#
# #################################################################################################################
#
# 3. Utilidade Prática: Conversão para JSON
#
# Está é uma das maiores utilidades: Transformar um objeto de uma classe em um formato que pode ser enviado para uma
# API ou salvo em um banco de dados NoSQL.
#
# Exemplo:
# 
# import json
#
# user_1 = Usuario("Renan Lima", "Desenvolvedor")
# user_1_dict = vars(user_1)
# print(user_1_dict)
#
# Convertendo o objeto para uma string JSON usando o vars() e o json.dumps():
# user_1_json = json.dumps(user_1_dict)
# print(user_1_json)
#
# #################################################################################################################
#
# 4. Manipulação Dinâmica de Atributos
#
# O atributo __dict__ não serve apenas para leitura. Você pode adicionar atributos ao objeto diretamente através dele
# (embora não seja uma prática comum no dia-dia, é útil em alguns casos como adicionar dinamicamente atributos a frameworks).
#
# Exemplo:
#
print("\nManipulação Dinâmica de Atributos com __dict__:")

user_1 = Usuario("Renan Lima", "Desenvolvedor")
user_1.__dict__["telefone"] = "1234-5678" # <- Atributo adicionado dinamicamente

print(f"\nAcrescentando um novo atributo ao user_1: {user_1.__dict__}") 
# Saída: {'nome': 'Renan Lima', 'cargo': 'Desenvolvedor', 'telefone': '1234-5678'}
# telefone foi adicionado ao dicinário da instância do user_1.__dict__ de forma dinâmica.
#
# também conseguimos alterar o valor dos atributos, exemplo: user_1.__dict__["nome"] = "Carlos Lima"
# conseguimos também apagar os atributos, exemplo: del user_1.__dict__["nome"]
#
# Exemplo para acrescentar um dicionário a uma classe:
#
# dados = {"nome": "Renan Lima", "cargo": "Desenvolvedor"}
# p1 = Pessoas(**dados) <- Desempacotei e recriei as instancias dentro da classe

#
# resumindo, tudo que funciona nos dicionários, funciona com o __dict__
#
# funciona com vars(): vars(user_1)["telefone"] = "1234-5678"
#
# #################################################################################################################
#
# 5. vars() vs. Atributos de Classe
#
# Um detalhe crucial para para um desenvolvedor Python: o __dict__ da instância mostra apenas o que foi deinifido no
# self. Ele não mostra os atributos de classe.
#
# #################################################################################################################
#
# --> Resumo Técnico
#
# Recurso      | O que é?                                 | Quando usar?
# -------------|------------------------------------------|-------------
# __dict__     | O dicionário interno de armazenamento    | Debbung profundo ou criação de frameworks(objetos dinâmicos).
# vars()       | Função que retorna o __dict__ de um obj  | Sempre que precisar converter um objeto para dict(API, JSON, etc).
#
# #################################################################################################################
#
# --> Nota de Performance(Engenharia de Software)
#
# Mesmo com uma grande quantidade de memória RAM, o uso do __dict__ é perfeitamente seguro. Porém, caso criemos vários
# objetos pequenos, o fato de cada um carregar um dicionário(__dict__) consumira muita memória. Nesses casos extremos,
# desenvolvedores usam o __slots__ para desabilitar o uso de __dict__ e garantir um menor consumo de memória.
#
# exemplo:
#
# class Usuario:
#     __slots__ = ["nome", "cargo"]
#     def __init__(self, nome, cargo):
#         self.nome = nome
#         self.cargo = cargo
#
# O __slots__ definem o únicos atributos permitidos é um sistema de arrays, quando desabilitamos o uso do __dict__:
#
# Meio que o slots diz ao Python: "Não use uma estrutura de dicionário padrão para os objetos, use uma estrutura dados
# fixos(um array de tamanho fixo) apenas para armazenar 'esses' atributos".
#
# #################################################################################################################
#
# ----- FIM ------
#
# ##################################################################################################################