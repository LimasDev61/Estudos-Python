# Encapsulamento(Modificadores de Acesso: Public, _Protected, __Private)
#
# #############################################################################################################
#
# Encapsulamento é o primeiro pilar da Porgramação Orientada a Objetos(POO). Na Engenharia de Software, ele serve
# para esconder os detalhes internos de como um objeto funciona e expor a apenas o necessário.
#
# Diferente das linguagens como JAVA e C#, onde o ocmpilador bloqueia o acesso a dados privados, o Python adota
# uma filosofia de que "somos todos adultos responsáveis". Os modificadores em Python são mais como "avisos" e
# conveção de nomêclatura.
#
# #############################################################################################################
#
# 1. Public(Público)
#
# Qualquer atributo ou método que não começa com underline(_), é public. Ele pode ser acessado e alterado de 
# qualquer lugar(dentro ou fora da classe).
#
# class Carro:
#     def __init__(self, modelo):
#         self.modelo = modelo
# 
#
# modelo = Carro("Fusca")
# print(modelo.modelo) # <- Acesso público: Fusca
# modelo.modelo = "Palio" <- Alteração pública permitida: Palio
# print(modelo.modelo) # Palio
#
# #############################################################################################################
#
# 2. Protected(Protegido)
#
# Atributos que começam com um único underline(_).
#
# -> A Convenção: Indica que o atributo não deve ser acessado fora da classe ou de suas subclasses(Herança).
#
# -> A Realidade: O Python não impede acesso. É apenas um sinal de "por favor, não mexa aqui, isso é interno".
#
# class Banco:
#     def __init__(self):
#         self._taxa = 0.05 <- Atributo protegido
#
# itau = Banco()
# print(itau._taxa) # <- O Python permite, mas estariamos quebrando a convenção.
#
# a forma correta seria definir um getter e setter para trabalhar com os atributos protegidos.
#
# #############################################################################################################
#
# 3. Privado(Privado)
#
# Atributos que começam com dois underlines(__). Aqui o Python fica mais rigoroso usando uma técnica chamada de
# Name Mangling(Desfiguração de Nome).
#
# -> O que acontece: O Python altera o nome do atributo internamente para dificultar o acesso acidental fora da
# classe. 
#
# -> Objetivo: Evitar que subclasses sobrescrevam atributos internos por acidente.
#
# class Smartphone:
#     def __init__(self, senha):
#         self.__senha = senha # <- Atributo privado
#
#     def mostra_senha(self):
#         # Internamente, a classe acessa normalmente o atributo privado.
#         return self.__senha
#
# cel = Smartphone("1234")
# print(cel.__senha) # <- Erro(AttributeError): O Python não permite acesso diretamente.
#
# print(cel.mostra_senha()) # <- OK: Acessado via método de classe.
#
# #############################################################################################################
#
# 4. Como o Name Mangling funciona?
#
# Se formos teimosos e realmente precisarmos acessar um dado privado(útil para debugger), podemos usar o Name
# Mangling: _NomeDaClasse__nome_do_atributo.
#
# Acessando o dado "privado" do exemplo anterior com o Name Mangling:
#
# print(cel._Smartphone__senha) # Saída: 1234
#
# Atenção: Nunca faça isso em código de produção. Isso quebra a segurança e a arquitetura do sistema.
#
# #############################################################################################################
#
# 5. Resumo Comparativo
#
# Modificador              | Sintaxe              | Onde Acessar?           | Intenção
# -------------------------|----------------------|-------------------------|--------------------------------------
# Public                   | nome                 | Em qualquer lugar.      | Acesso livre.
# Protected                | _nome                | classes e subclasses.   | Não mexer se não for família.
# Private                  | __nome               | Apenas na classe atual. | Acesso Restrito: Interno da classe.
# -----------------------------------------------------------------------------------------------------------------
#
# #############################################################################################################
#
# -> Por que isso é vital para o Roadmap?
#
# No desenvolvimento Backend, poderemos usar:
#
# 1. Private(__): Uso para chaves de API, senhas e estados críticos que não podem ser alterado sem validação.
#
# 2. Protected(_): Uso para métodos auxiliares que você não quer que apareçam no preenchimento automático(IntelliSense)
# de quem usa sua bibliotéca, mas que podem ser úteis para quem herdar a classe.
#
# 3. Public(_): Uso para dados que podem ser alterados sem problemas(ex, em alguns casos: telefone de contato).
#
# ############################################################################################################
#
# ---- FIM ----
#
# ############################################################################################################