# Relações Entre Classes: Associação, Agregação e Composição
#
# ################################################################################################################
#
# As relações entre as classes definem como os objetos conversam e qual o nível de dependência entre eles.
# Entender a diferença entre associação, agregação e composição é o que separa um programador que escreve scripts
# de um que projeta sistemas escaláveis.
#
# ################################################################################################################
#
# 1. Associação (Relação "Usa Um")
#
# É a relação mais fraca. Os objetos são independentes e têm ciclos de vida próprios. Um objeto simplesmente utiliza
# o outro para realizar uma tarefa.
#
# - Exemplo: Um Escritor usa uma Caneta para Escrever. O escrito usa a caneta para escrever, mas se o escritor parar
# de existir, a caneta continua existindo(vice-versa).
#
# - No Código: Um objeto é passado como argumento ou armazenado como atributo, mas não "pertence" ao outro.
#
# - Exemplo de Código:
#
# class Escritor:
#     def __init__(self, nome):
#         self.nome = nome
#         self.ferramenta = None
#
# class Caneta:
#     def escrever(self):
#         print("A caneta está escrevendo...")
#
# escritor = Escritor("Renan")
# caneta_azul = Caneta()
# 
# # Associação: o escritor passa a usar a caneta:
#
# escritor.ferramenta = caneta_azul <- armazenando a caneta no escritor
# escritor.ferramenta.escrever() # A caneta está escrevendo...
#
# ################################################################################################################
#
# 2. Agregação (Relação "Tem Um")
#
# É uma forma especializada de associação. Indica uma relação de toda/parte, mas as partes podem existir sem o todo.
# O todo não é dono absoluto da existência parte.
#
# - Exemplo: Um CarrinhoDeCompras e um Produto. O carrinho pode conter produtos. Se deletar o carrinho(fechar o app),
# o produto continua existindo no banco de dados da loja.
#
# - No Código: A classe principal(todo) recebe os objetos já criados de fora e armazena-os como atributos.
#
# - Exemplo de Código:
#
# class CarrinhoDeCompras:
#     def __init__(self):
#         self.produtos = []
#
#     def adicionar_produto(self, produto):
#         self.produtos.append(produto) 
#
# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco
#
# carrinho = CarrinhoDeCompras()
# produto = Produto("Caneta", 2.5)
# 
# # Agregação: o carrinho passa a conter o produto:
#
# carrinho.adicionar_produto(produto) <- armazenando a instância da classe Produto na classe CarrinhoDeCompras.
#
# ################################################################################################################
#
# 3. Composição (Relação "É dono de...")
#
# É a relação mais forte(morte mútua). A parte só existe enquanto o todo existir. Se o objeto principal for destrúido
# todos os objetos que ele compõe também serão destruídos da memória.
#
# - Exemplo: Um Cliente e seu Endereço. No sistema da empresa, se o cliente for deletado, não fará sentido manter o 
# endereço dele no banco de dados. O Endereço morre junto ao cliente.
#
# - No Código: A classe principal(todo) instância os objetos dependentes dentro dela.
#
# - Exemplo de Código:
#
# class Cliente:
#     def __init__(self, nome):
#         self.nome = nome
#         self.endereco = []
#
#     def insere_endereco(self, cidade, estado):
#         # Composição: o objeto Endereço é criado dentro da classe Cliente.
#         self.endereco.append(Endereco(cidade, estado))
#
# class Endereco:
#     def __init__(self, cidade, estado):
#         self.cidade = cidade
#         self.estado = estado
#
# cliente = Cliente("Renan")
# 
# Composição: o cliente passa a conter o endereço
# cliente.insere_endereco("São Paulo", "SP")
#
# print(f"O cliente {cliente.nome} mora na cidade {cliente.endereco[0].cidade} no estado {cliente.endereco[0].estado}.")
# Saída: O cliente Renan mora na cidade São Paulo no estado SP. 
#
# Se deletarmos o cliente, os objetos de endereço também serão deletados:
# del(cliente)
# print(cliente.endereco) # Erro: o endereço morreu junto ao cliente
#
# ################################################################################################################
#
# 4. Resumo de Engenharia das Relações
#
# Relação       | Força             | Ciclo de Vida      | Analogia
# --------------|-------------------|--------------------|------------------------------------------------------------------------
# Associação    | Fraca             | Independente       | Motorista e Carro(O motorista sai e entra em outro carro).
# Agregação     | Média             | Independente       | Professor e Escola(A escola fecha, mas o professor continha existindo).
# Composição    | Forte             | Dependente         | Coração Humano(O Coração não sobrevive sem o corpo).
# --------------|-------------------|--------------------|------------------------------------------------------------------------
#
# ################################################################################################################
#
# -> Por que isso importa no Roadmap?
#
# Essas distinções ajudam no Gerenciamento de Memória e nos Design Patterns.
#
# - Em Agregação, podemos compartilhar objetos entre classes para uma lógica maior(Economizando RAM).
#
# - Em Composição, garantimos que a integridade dos dados (não deixa "lixo" ou dados orfãos) no sistema.
#
# - Em Associação, podemos reutilizar os objetos criados fora da classe principal. <- Raramente usado em Python.
#
# ################################################################################################################
#
# ---- FIM ----
#
# ################################################################################################################