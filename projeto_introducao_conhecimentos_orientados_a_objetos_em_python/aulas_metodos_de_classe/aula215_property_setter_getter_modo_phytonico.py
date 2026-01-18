# @property + @setter, getter e setter no modo Pythônico
#
# #############################################################################################################
#
# Para um Engenheiro de Software, o par @property e @setter representa o ápice do Encapsulamento em Python. Eles 
# permitem que possamos proteger os dados sem sacriar a simplicidade do código.
#
# Enquanto o @property(getter) controla a saída/leitura do dado. O @setter controla a entrada/escrita, permitindo
# que você valide as informações antes que elas "sujem" o estado do objeto.
#
# #############################################################################################################
#
# 1. A Sintaxe do @setter
#
# Para criar um setter, temos primeiro que ter um getter(@property) definido. O nome do decorador do setter será
# sempre @nome_da_property.setter.
#
# Exemplo:

class Smartphone:
    def __init__(self, modelo, preco):
        self.modelo = modelo
        # Usamos o " _ "(protected) para indicar que não deve ser acessado diretamente.
        self.preco = preco # <- Chamei o setter, ja na construção do objeto

    @property
    def preco(self):
        # Este é o getter: ele "disfarça" o método como um atributo.
        print("\nAcessando o preço via property(getter):")
        return f"O Preço do Smartphone {self.modelo} é R$ {self._preco:,.2f}"

    @preco.setter
    def preco(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("\nO preço precisa ser numérico.")
        
        if valor < 0:
            raise ValueError("\nO preço precisa ser maior ou igual a zero.")

        self._preco = valor # protected no local correto.

# Uso Prático
try:
    item = Smartphone("Iphone 14", 10000) # <- se o protected estivesse dentro do init, permitiria o valor negativo
    # por isso é chamado no setter.

    print(item.preco) # Acessando o preço via property(getter), saída: O Preço do Smartphone Iphone 14 é R$ 10.000.

    print(20 * "-")
    print("\n(Pausa) Aqui, alterei o preço via setter...")
    # O Python redireciona o " = " automáticamente para o método @preco.setter.
    item.preco = 5000 # Alterando o preço via setter, saída: Alterando o preço via setter

    print(item.preco) # Acessando o preço via property(getter), saída: O Preço do Smartphone Iphone 14 é R$ 5.000.
    print(20 * "-")
    # Testando o erro
    print("\n(Pausa e Erro) Aqui, alterei o preço via setter, para um valor negativo...")
    item.preco = -1000
except ValueError as e:
    print(e)

# Mantém o valor antigo, saída: O Preço do Smartphone Iphone 14 é R$ 5.000.

# #############################################################################################################
#
# 2. Por que usar o setters em vez de Atributos Públicos?
#
# No roadmap de Backend e Engenharia de Software, isso é crucial por três motivos:
#
# 1. Validação de Dados: Garante que o estado do objeto seja sempre consistente(ex: idade não pode ser negativa, 
# e-mail deve ter @).
#
# 2. Transformação Automática: Podemos converter os dados de entrada(ex: transformar o nome em Title Case, sempre
# que ele for alterado).
#
# 3. Logs e Auditoria: Podemos registrar em um arquivo de log toda vez que um valor sensível(como saldo de um cliente)
# for modificado.
#
# #############################################################################################################
#
# 3. Resumo de Boas Práticas(PeP 8):
#
# -> Não use getters/setters se não precisar: Se um atributo é apenas um dado simples que não precisa de validação,
# deixe o público. Em Python: "Somos todos adultos responsáveis".
#
# -> Use para Evolução: Se um atributo público precisar de validação no futuro, você o transformar em @property 
# sem quebrar o código de quem o utiliza.
#
# -> Encapsulamento: User o underline(_preco) para o atributo real, indicando que ele é privado e o acesso deve ser
# feito pela property(getter) e setter.
# 
# #############################################################################################################
# 
# ---- FIM ---- 
#
# ############################################################################################################