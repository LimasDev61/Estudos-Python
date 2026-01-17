# @staticmethod(métodos estáticos) são inúteis?
#
# #########################################################################################################
#
# Se pensarmos apenas em termos "funcionalidade", nós temos um ponto: tudo que um @staticmethod faz, uma
# função solta no topo do seu arquivo .py também faz.
#
# No entanto, a "utilidade" vai além de fazer o código rodar, ela entra no campo de organização, semântica
# e design de código.
#
# Mas a questão é, @staticmethod é útil? Vamos descobrir.
#
# #########################################################################################################
#
# 1. Organização e Namespace(Espaço de nomes)
#
# Imagine que temos uma classe ProcessarPagamento. Para processar um pagamento, precisamos validar o CPF.
#
# Poderiamos colocar essa função validar_cpf() solta o arquivo. Mas, se essa validação só faz sentido dentro
# do contexto de pagamentos, colocá-la dentro da classe como um @staticmethod seria muito mais adequado para
# manter o namespace limpo.
#
# Exemplo, sem o @staticmethod: O validar_cpf()flutuando no módulo.
#
# def validar_cpf(cpf):
#     return len(cpf) == 11
#
# class ProcessarPagamento:
#     def processar(self, valor, cpf):
#         if validar_cpf(cpf):
#             # ...
#         # ...
#
# -> Organização(Namespace): A função validar_cpf() está no escopo global, podendo causar conflitos em 
# arquivos grandes.
#
# -> Chamada: validar_cpf("123...")
# 
# 
# Exemplo, com o @staticmethod: temos ProcessarPagamento.validar_cpf(). Fica óbvio a quem essa útilidade
# pertence.

class ProcessarPagamento:
    @staticmethod
    def validar_cpf(cpf):
        return len(cpf) == 11
    
    def processar(self, valor, cpf):
        # Aqui útilizamos o @staticmethod para validar o CPF
        if self.validar_cpf(cpf):
            print(f"Pagamento de R$ {valor} efetuado com sucesso!")

resultado = ProcessarPagamento()

resultado.processar(100, "12345678910") # Saída: Pagamento de R$ 100 efetuado com sucesso!

# Também posso utilizar apenas o @staticmethod para validar o CPF antes de instanciar a classe.
#
# -> Organização(Namespace): A útilidade pertence ao namespace da classe, indicando sua finalidade em
# específico.
#
# -> Chamada: ProcessarPagamento.validar_cpf("123...")
#
# ########################################################################################################
#
# 2. Sinalização de Intenção(Semântica)
#
# Quando você(ou alguém da sua equipe) lê um código e vê @staticmethod, o cérebro recebe um aviso imediato:
#
# "Essa função não altera nada no objeto(self) e nem nada classe(cls). Ela é pura e independente."
#
# Isso facilita muito o debug e a manutenção, pois você sabe que chamar aquele método não terá efeitos colaterais
# no estado do sistema.
#
# ########################################################################################################
#
# 3. Comparação Definitiva
#
# Tipo de Método | Decorador       | Recebe o que?  |  Quando usar?
# ---------------|-----------------|----------------|----------------------------------------------------
# Instância      |   N/A           | self(objeto)   | Quando for acessar dados(ex: self.nome).
# Classe         |   @staticmethod | cls(classe)    | Para criar fábricas e mudar o estado da classe.
# Estatico       |   @staticmethod | N/A            | Funções utilitarias que pertencem aquele contexto.
# ---------------|-----------------|----------------|----------------------------------------------------
# 
# ########################################################################################################
#
# 4. Exemplo Prático: Utilitário de Backend
#
# No roadmap de Backend, lidamos muito com validações. Veja como o código fica mais profissional:


print(20 * "-")
print("\nExemplo Prático: Utilitário de Backend\n")
class ValidadorFintech:
    def __init__(self, usuario):
        self.usuario = usuario

    @staticmethod
    def formatar_moeda(valor):
        # Não precisamos de dados da classe ou usuario para formatar um número.
        return f"R$ {valor:,.2f}"
    
    def gerar_extrato(self, saldo):
        # Uso do método estático internamente.
        valor_formatado = ValidadorFintech.formatar_moeda(saldo)
        return f"Usuario: {self.usuario}\nSaldo atual: {valor_formatado}"

# Uso direto da utilidade sem precisar instânciar.
print(ValidadorFintech.formatar_moeda(1500.5)) # Saída: R$ 1,500.50

instanciar = ValidadorFintech("Renan Lima")
print(instanciar.gerar_extrato(1500.5)) # Saída: Usuario: Renan Lima\nSaldo atual: R$ 1,500.50

# ########################################################################################################
#
# -> Quando eles são inúteis?
#
# Se estamos criando um script pequeno de automação ou um notebook de análise de dados rápido, o @staticmethod
# é realmente overhead(despesa) desnecessário. Uma função simples resolve o problema.
#
# Porém, em sistemas grandes, a agrupagem lógica que o @staticmethod oferece é o que mantém o código sustentável.
# Podemos carregar bibliotecas gigantescas; manter o que é de cada classe bem guardado evitando colisão de nomes.
#
# ########################################################################################################
#
# -> Resumo de Engenharia
#
# Não podemos ver o @staticmethod como uma "função especial", mas como uma etiqueta de organização. Ele diz:
# "Moro aqui dentro desta classe porque sou parente desta lógica, mas sou independente da classe e do objeto."
#
# ########################################################################################################
# 
# ---- FIM ------
#
# ########################################################################################################