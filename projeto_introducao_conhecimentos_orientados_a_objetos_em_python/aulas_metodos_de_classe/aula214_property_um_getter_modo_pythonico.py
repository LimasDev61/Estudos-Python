# @property - um getter no modo Pythônico
#
# #############################################################################################################
#
# O decorador @property é a solução elegante do Python para um problema clássico da Engenharia de Software: Como
# acessar ou válidar dados de um objeto sem quebrar o código de quem o utiliza.
#
# Em linguagens como JAVA, você é obrigado a usar get_valor() e set_valor(). No Python, o @property permite que
# você transforme um método em algo que parece um atributo comum mas que executa uma lógica por trás.
#
# #############################################################################################################
#
# 1. O Problema: Acesso Direto vs. Validação
#
# Imagine que você tem uma classe ContaBancaria. Se o saldo for um atributo público, qualquer um pode acessar e
# fazer isso conta.saldo = -1000, o que é um erro de négocio e segurança.
#
# Se começar com um atributo público e depois precisar adicionar uma regra de validação, teria que muda conta.saldo
# para conta.get_saldo() em todo o sistema, quebrando o código dos outros desenvolvedores.
#
# #############################################################################################################
#
# 2. Solução: Usar o @property(O getter)
#
# Com o @property, podemos também manter a interface limpa(usando o . ), ganhando controle total sobre o que
# acontece na leitura do dado.
#
# Exemplo:

class Smartphone:
    def __init__(self, modelo, preco):
        self.modelo = modelo
        # Usamos o " _ "(protected) para indicar que não deve ser acessado diretamente.
        self._preco = preco

    @property
    def preco(self):
        # Este é o getter: ele "disfarça" o método como um atributo.
        print("Acessando o preço via property.")
        return f"O Preço do Smartphone {self.modelo} é R$ {self._preco:,.2f}"
    

# Uso Prático

smartphone = Smartphone("Xiaomi", 2000)

# Note que não usamos parênteses: smartphone.preco() causaria erro. Chamamos como se fosse uma variável
# comum.
print(smartphone.preco) # Saída: Acessando o preço via property.O Preço do Smartphone Xiaomi é R$ 2,000.00

# ################################################################################################
#
# 3. Por que isso é Pythônico?
#
# A filosofia do Python diz que "deve haver preferencialmente apenas uma maneira óbvia de fazer algo".
# Portanto, o @property segue isso ao permitir que:
#
# 1. Compatibilidade Retroativa: Podemos transformar um atributo real em uma property sem que ninguém
# precise mudar uma linha de código que consome sua classe.
#
# 2. Atributos Calculados: Você pode criar atributos que não existem fisicamente, mas podem ser calculados
# na hora por meio de um getter.
#
# Exemplo:

# class Retangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     @property
#     def area(self):
#         # A área não precisa ser "salva", ela é calculada sob demanda.
#         return self.base * self.altura

# # Uso Prático

# retangulo = Retangulo(10, 20)
# print(retangulo.area) # Saída: 200

# #################################################################################################
#
# 4. Resumo de Engenharia para o Roadmap
#
# Recurso                 | Função                              | Benefício
# ------------------------|-------------------------------------|-------------------------------------
# Atributo Interno(_nome) | Armazena o valor real.              | Esconde o dado "cru".
# @poperty                | Disponibiliza o dado para leitura   | Permite formatar ou logar o acesso.
# Interface Limpa         | Chamada via objeto.nome             | Facilita a vida de quem usa a classe.
# ------------------------|-------------------------------------|-------------------------------------
#
# #################################################################################################
# 
# ----- FIM -----
#
# ################################################################################################