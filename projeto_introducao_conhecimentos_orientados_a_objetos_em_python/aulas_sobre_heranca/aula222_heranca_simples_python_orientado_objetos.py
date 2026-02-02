# Herança Simples em Python - Orientação a Objetos
#
# ################################################################################################################
#
# A Herança Simples acontece quando uma subclasse(filha) herda de apenas uma superclasse(pai). No Python, isso é a base
# para criar hierarquias de códigos claras e organizadas, permitindo que a classe filha aproveite todos os atributos e
# métodos de classe pai como se fossem dela.
#
# A herança simples é sua melhor companheira para manter o código DRY (Don't Repeat Yourself - Não se Repita).
#
# ################################################################################################################
#
# 1. A Sintaxe da Herança
#
# Para fazer uma classe herdar de outra, basta passar a classe pai entre parênteses na definição da classe filha:
# class Filha(Pai):.
#
# Classe Pai:
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome(self):
        return f'Meu primeiro nome é: {self.nome}, meu sobrenome é: {self.sobrenome}'
    
# Aluno(Filha) HERDA de Pessoa(Pai)
class Aluno(Pessoa):
    def estudar(self):
        return f'{self.nome} está estudando...'
    
aluno = Aluno('João', 'Silva')
print(aluno.falar_nome())  # Herdado de Pessoa -> Meu primeiro nome é: João, meu sobrenome é: Silva
print(aluno.estudar())  # Método próprio de Aluno -> João está estudando...
#
# ################################################################################################################
#
# 2. A Função super()
#
# Na Engenharia de Software, raramente a classe filha é apenas uma "cópia" da pai. Geralmente, ela precisa de atributos
# extras. Para isso, usamos a função super(), que permite chamar o construtor(ou qualquer outro método) da classe 
# superior.
#
# class Cliente(pessoa):
#     def __init__(self, nome, sobrenome, id_cliente):
#         # chama o __init__ de pessoa para configurar nome e sobrenome
#         super().__init__(nome, sobrenome)
#         # configura o atributo exclusivo de cliente
#         self.id_cliente = id_cliente
#
# c1 = Cliente("carlos", "silva", 1024)
# c1.falar_nome() # Herdado de Pessoa -> Meu primeiro nome é: carlos, meu sobrenome é: silva
# print(f"id: {c1.id_cliente}")
#
# ################################################################################################################
#
# 3. Sobreposição de Métodos (Method Overriding)
#
# Às vezes, o comportamente da classe pai não é exatemente o que queremos na classe filha. Nesse caso, podemos
# "sobrescrever" o método simplesmente criando um com o mesmo nome na subclasse.
#
print("\nSobreposição de Métodos (Method Overriding):")
class Professor(Pessoa):
    def falar_nome(self):
        return f'Professor {self.nome} {self.sobrenome} está falando.'
    
professor = Professor('Ana', 'Oliveira')
print(professor.falar_nome())  # Professor Ana Oliveira está falando. <- Saída customizada
#
# ################################################################################################################
#
# 4. Vantagens no Seu Roadmap de Engenharia
#
# -> Manutenibilidade: Se você precisar adicionar um atributo "email" a todas as pessoas do sistema(Alunos, Professores,
# Clientes), podemos alterar apenas a classe Pessoa.
#
# -> Organização Lógica: Com um sistema de herança bem estruturado, podemos criar milhares de tipos de objetos. A Herança
# garante que você saiba exatemente onde procurar um comportamente específico(se não está na classe filha, provavelmente está
# na classe pai).
#
# -> Extensibilidade: Podemos criar uma nova especialização(ex: AlunoBolsista) herdando de Aluno, sem tocar no código que já
# funciona.
#
# ################################################################################################################
#
# * Resumo Técnico:
#
# Termo             Função
#
# Superclasse       A classe(pai) que contém o código geral a ser herdado.
# Subclasse         A classe derivada(filha) que especializa o código da superclasse(pai).
# super()           Ponte para acessar métodos e atributos da superclasse(pai) dentro da subclasse(filha), sem citar o nome dela.
# Override          Ato de redefinir um método da superclasse(pai) na subclasse(filha) para alterar seu comportamente.
#
# Dica de Engenharia: Embora a Herança Simples seja poderosa, evite criar hierarquias muito profundas(Pai -> Filho -> 
# Neto -> Bisneto...). Isso torna o código dfícil de rastrear. Tente manter a "árvore" mais rasa o pessivel(Pai -> 
# Filho -> Neto(no máximo até o terceiro nível)).
# 
# A class faz parte do builtins object do Python, então todas as classes pai herdam(extendem) de object implicitamente.
#
# para verificar isso, execute: help(NomeDaSuaClasse), ele vai mostrar que sua classe pai herda de builtins object.
#
# Exemplo:
# class Foo():
#     pass
# 
# help(Foo)
#
# Output:
#
# Help on class Foo in module __main__:
#
# class Foo(builtins.object) <-- Herda de builtins.object
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables
#  |
#  |  __weakref__
#  |      list of weak references to the object
#
# ################################################################################################################
# 
# --- FIM ---
#
# ################################################################################################################