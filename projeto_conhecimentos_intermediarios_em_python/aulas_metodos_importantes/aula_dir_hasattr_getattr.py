# As funções dir(), hasattr() e getattr() em Python são ferramentas poderosas
# e fundamentais para inspecção de objetos e manipulação de atributos de forma
# dinâmica e flexível.
# Dir() mostra todos os atributos e métodos de um objeto, funciona 
# como uma biblioteca.
# Hasattr() verifica se um objeto possui um atributo ou método, retorna True
# ou False.
# Getattr() obtem o valor de um atributo de um objeto, pode ter um valor padrão.

# Sintaxe
# Dir: dir(objeto)
# Hasattr: hasattr(objeto, 'atributo')
# Getattr: getattr(objeto, 'atributo', valor_padrao)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Joaquim", 25)
pessoa1 = Pessoa("Renan", 33)

print("Todos os metodos e atributos de uma string que podem ser usados:", \
        dir(pessoa))

print("\nVerifica se um objeto possui um atributo ou método:", \
        hasattr(pessoa, "nome"))

print("\nObtem o valor de um atributo de um objeto:", getattr(pessoa, "nome"))

# O getattr pode ter um valor padrão, caso o atributo não seja encontrado
print("\nVerifica se um objeto possui um atributo ou método:", \
        getattr(pessoa1, "meses", "meses não encontrado - valor padrão"))

# Verificar se o método existe
print("\nVerifica se um objeto possui um atributo o método 'falar':")
if hasattr(pessoa, "falar"):
    pessoa.falar()
else:
    print("Metodo não encontrado")

# Funsão do getattr e hasattr
print("\nVerifica se um objeto possui um atributo o método 'upper':")
if hasattr(pessoa, "nome"):
    print("Existe Upper")
    print(getattr(pessoa, "nome").upper())
else:
    print("Metodo não encontrado")

# Quando não encontra
print("\nVerifica se um objeto possui um atributo o método 'upper':")
if hasattr(pessoa, "upper"):
    print("Existe Upper")
    print(getattr(pessoa, "upper"))
else:
    print("Metodo não encontrado")

atributos = dir(pessoa)
print(atributos[:5])  # Mostra os 5 primeiros atributos e métodos