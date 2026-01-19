# Agregação Python - Orientado a Objetos
#
# ################################################################################################################
#
# A Agregação é considerada uma relação fraca/média ou externa, pois as partes podem existir independentes do objeto
# príncipal.
#
# ################################################################################################################
#
# 1. O Conceito: "Tem Um"(Has-a)
#
# Na Agregação, uma classe(o todo) precisa de outra classe(a parte) para executar a sua função completa, mas ela 
# não é "dona" do ciclo de vida daquela parte.
#
# -> Exemplo Clássico: Um CarrinhoDeCompras(Todo) e um Produto(Parte).
#
# -> A Lógica: Se excluirmos o carrinho, os produtos não devem sumir do sistema, pois eles ainda existem no estoque
# da loja.
#
# ################################################################################################################
#
# 2. Implementação em Python
#
# A príncipal característica técnica da agregação é que o objeto parte é criado fora do objeto todo e depois passado
# para ele(geralmente via método ou no __init__).
#
# Exemplo de Código:
#
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, *produtos):
        # o carrinho agrega os produtos que ja existem fora dele
        for produto in produtos:
            self.produtos.append(produto)

    def somar_produtos(self):
        return sum([p.preco for p in self.produtos], 0)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Execução:

# Criamos os produtos de forma independente
produto1 = Produto("Caneta", 3)
produto2 = Produto("Lapis", 2)
produto3 = Produto("Borracha", 1)

# Criamos o carrinho de compras e Agregamos os produtos
carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(produto1, produto2, produto3)

# Listamos os produtos
print("\nProdutos no carrinho:")
carrinho.listar_produtos()

# Retorna o valor total dos produtos
print(f"\nTotal dos produtos somados no carrinho: R$ {carrinho.somar_produtos():,.2f}")

# Se eu deletar meu carrinho:
# del carrinho
#
# Os produtos cóntidos dentro do bd/instâncias na memória, continuam existindo.
#
# ################################################################################################################
#
# -> Por que usar Agregação no Roadmap?
#
# 1. Reutilização de Objetos: Podemos usar o mesmo objeto Produto em um CarrinhoDeCompras, em uma ListaDeDesejos e
# em um RelatorioDeVendas simultaneamente, isso economiza RAM.
#
# 2. Manutenção: Se a classe Produto mudar, podemos alterar em um lugar sem afetar o outro.
#
# 3. Testabilidade: ´Muito mais fácil testar a classe CarrinhoDeCompras, passando objetos falsos(mocks) de produtos
# para ela.
#
# ################################################################################################################
#
# ---- FIM ----
#
# ################################################################################################################