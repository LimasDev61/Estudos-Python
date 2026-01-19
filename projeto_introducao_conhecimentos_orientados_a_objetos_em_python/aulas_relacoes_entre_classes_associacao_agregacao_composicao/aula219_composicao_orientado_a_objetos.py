# Composição - Python Orientado a Objetos
#
# ################################################################################################################
#
# A Composição é a relação mais forte entre duas classes. Ela representa uma relação de todo/parte onde a parte não
# existe sem um todo.
#
# Diferente de Agregação(onde "alugamos" um objeto externo), na Composição a classe PRINCIPAL é a dona do ciclo de
# vida dos objetos que a compõe. Se o objeto principal for deletado da memória/bd, todos os seus componentes serão
# destruídos com ele.
#
# ################################################################################################################
#
# 1. O Conceito: "Morte Mútua"(Is-a)
#
# Pense em um Cliente e seus Endereços. No banco de dados de um e-commerce, se você excluir a conta de um cliente,
# não faz sentido manter os endereços dele orfãos no sistema. O Endereço é uma parte intríseca do registro do cliente
# naquela aplicação.
#
# ################################################################################################################
#
# 2. Implementação em Python
#
# A característica técnica da composição é que o objeto filho(parte) é instanciado dentro da classe pai(todo).
#
# Exemplo de Código:
#
# Classe Pai:
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, cidade, estado):
        # Composição: O objeto endereço(filho) é criado aqui dentro. Ele pertence exclusivamente ao objeto pai.
        self.enderecos.append(Endereco(cidade, estado))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        # Este método é chamado quando o objeto é deletado da RAM, no final da execução.
        print(f"\nO cliente {self.nome} foi deletado, seus endereços também foram deletados.")

# Classe Filho:
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

# Execução:

# Instanciando o objeto pai
cliente = Cliente("Renan")

# Adicionando o primeiro endereço
endereco = cliente.inserir_enderecos("São Paulo", "SP")

# Adicionando o segundo endereço
endereco = cliente.inserir_enderecos("Rio de Janeiro", "RJ")

# Listando os endereços
print("\nListando os endereços do cliente:")
cliente.listar_enderecos()

# Deletando o cliente
del(cliente)

# ################################################################################################################
#
# 3. Vantagens e Cuidados na Engenharia
#
# - Encapsulamento Total: Quem usar a classe Cliente não precisa nem saber que a classe Endereço existe. Tudo é
# resolvido através do cliente.
#
# - Integridade dos Dados: Garante que não existam objetos "lixo"(leaking) na memória. Se o pai morre, os filhos
# morrem.
#
# - Atenção: A composição cria um alto acoplamento. Se mudar o __init__ da classe Endereco, terá que obrigatóriamente
# mudar o método inserir_enderecos() dentro da classe Pai(Cliente).
#
# ################################################################################################################
#
# ---- FIM ----
#
# ################################################################################################################