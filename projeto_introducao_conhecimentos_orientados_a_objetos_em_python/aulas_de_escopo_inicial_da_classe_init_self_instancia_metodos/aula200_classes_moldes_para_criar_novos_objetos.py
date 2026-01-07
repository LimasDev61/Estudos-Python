# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    ...


# Criando uma instância (objeto) da classe Pessoa
p1 = Pessoa() # <- criando o objeto p1
#
# Criando dados para o objeto p1, ou seja, atributos.
p1.nome = "Renan"
p1.sobrenome = "Lima"
p1.idade = 23

print(f"Nome: {p1.nome} {p1.sobrenome} Idade: {p1.idade}") # <- Acessando os atributos do objeto p1

# Mas a classe está vazia, ou seja, não possui nenhum atributo
# Isso não é legal, pois toda vez que criamos um novo objeto
# da classe Pessoa, teremos que criar os atributos manualmente.
# o que pode causar erros e inconsistências.
# Exemplo:

p2 = Pessoa()
p2.nome = "Renan"
p2.sobrenome = "Lima"

# p2.idade = 23  <- esqueceu de criar o atributo idade
print(f"Nome: {p2.nome} {p2.sobrenome} Idade: {p2.idade}") # <- Acessando os atributos do objeto p2
# AttributeError: 'Pessoa' object has no attribute 'idade' -> pois o atributo idade não foi criado.
# Isso ocorre porque a classe Pessoa foi criada sem atributos, e não pode padronizar os dados dos objetos.
# inclusive, se tentarmos acessar um atributo que não existe, teremos um erro. Assim como podemos
# criar o objeto passando os valores que quisermos, o que pode gerar inconsistências.
# má prática!

#
# 2. Porque usar classes?
#
# Usamos classes para agrupar dados e funcionalidades relacionadas em um único lugar.
# Isso nos ajuda a organizar melhor o código, facilitando a manutenção e reutilização.
#
# Vantagens de usar classes:
#
# Consistencia: Todos os objetos "pessoa" terão obrigatóriamente os mesmos atributos.
# Encapsulamento: Podemos esconder detalhes internos e expor apenas o que é necessário.
# Reutilização: Podemos criar múltiplos objetos a partir da mesma classe.
# Manutenção: Facilita a atualização e modificação do código.
# Herança: Podemos criar novas classes baseadas em classes existentes.
# Polimorfismo: Podemos usar uma interface comum para diferentes tipos de objetos.

# Resumo de Conceitos Importantes:
#
# Termo         | Definição                                         | Analogia
# --------------|---------------------------------------------------|-----------------------
# Classe        | Molde para criar novos objetos                    | Planta baixa de uma casa.
# Objeto        | A váriavel que armazena a instância               | Casa construída a partir da planta.
# Atributo      | Variável dentro de uma classe                     | Características da casa, como cor, tamanho, etc.
# Métodos       | Funções dentro de uma classe                      | Comportamentos da casa, como abrir a porta, acender as luzes, etc.
# Instância     | Objeto criado a partir de uma classe              | Casa construída a partir da planta.
# self          | Referência para a própria instância do objeto     | O "eu" dentro da casa, referenciando a própria casa.
