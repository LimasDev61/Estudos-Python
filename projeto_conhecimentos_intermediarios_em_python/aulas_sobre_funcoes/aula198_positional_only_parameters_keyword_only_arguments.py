# Positional-Only e Keyword-Only Arguments

# Python 3.8 introduziu novos argumentos de funções, chamados Positional-Only e
# Keyword-Only Arguments.
#
# Essa é a maneira mais refinada de controlar a interface das funções em Python.
# Ao usar " / " (barra) e " * "(asterisco), ditamos exatamente como outros desenvolvedores
# (ou nós mesmos no futuro) devem chamar a função.
#
# Esses recursos servem para evitar ambiguidades e garantir que as assinaturas das funções 
# sejam mais robustas(resistam aos erros comuns).
#
# -------------------------------------------------------------------------------------------------

# 1. Parâmetros Positional-Only(/)
#
# Tudo que vem antes da barra(/) deve ser passado obrigatoriamente por posição. Não podemos
# usar o nome do argumento na chamada.
#
# -> Porque usar?
#
# - Quando o nome do argumento não importa ou pode ser alterado no futuro.
#
# - Para imitar o comportamento de funções nativa escritas em C(como len() ou abs()).
#
# ----- Exemplo(/):
#
# 'nome' e 'idade' são apenas posicionais
# def registrar_usuario(nome, idade, /):
#     print(f"Usuário: {nome}, Idade: {idade}")
#
# ✅ CORRETO:
# registrar_usuario("Renan", 30)
#
# ❌ ERRO (TypeError):
# registrar_usuario(nome="Renan", idade=30)
#
# -------------------------------------------------------------------------------------------------

# 2. Parâmetros Keyword-Only(*)
#
# Tudo o que vem depois do asterisco(*) deve ser passado obrigatoriamente por nome(chave).
#
# -> Porque usar?
#
# - Segurança: Evita que o usuário passe valores na ordem errada, o que é perigoso em 
# funções com muitos parâmetros booleanos ou configuráveis.
#
# - Legibilidade: Obriga o código de quem chama a ser explicito
# (ex: enviar_email(urgente=True)) em vez de apenas enviar_email(True).
#
# ----- Exemplo(*):
#
# 'mensagem' pode ser posicional ou nomeado
# 'destinatario' e 'urgente' DEVEM ser nomeados
# def enviar_notificacao(mensagem, *, destinatario, urgente=False):
#     print(f"Enviando '{mensagem}' para {destinatario} (Urgente: {urgente})")
#
# ✅ CORRETO:
# enviar_notificacao("Olá!", urgente=True, destinatario="admin@email.com")
# a ordem dos argumentos nomeados não importa.
#
# ❌ ERRO (TypeError):
# enviar_notificacao("Olá!", "admin@email.com", True)
#
# -------------------------------------------------------------------------------------------------

# 3. A Função "Híbrida"((Positional-Only + Keyword-Only) O padrão Ouro)
#
# Podemos combinar os dois na mesma função para ter controle total da interface ou API.
# A ordem é sempre:
#
# 1. Parâmetros Positional-Only (/)
# 2. Parâmetros Padrão (posicionais ou nomeados)
# 3. Parâmetros Keyword-Only (*)
#
# ----- Exemplo(Híbrido -> / + *):
#
# def configurar_servidor(ip, porta, /, timeout=30, *, log_level="INFO"):
    # ip, porta -> Apenas posição
    # timeout   -> Pode ser posição ou nome (Híbrido)
    # log_level -> Apenas nome
#   pass
#
# Exemplo de chamada válida:
# configurar_servidor("192.168.0.1", 8080, 60, log_level="DEBUG")
#
# / -> ip e porta são posicionais
# Standard -> timeout pode ser posicional ou nomeado(ex: timeout=60 ou 60)
# "*" -> log_level deve ser nomeado
#
# ------------------------------------------------------------------------------------------------

# 4. Resumo Visual das Regraes:
#
# Símbolo    |  Nome                |  Exemplo de Uso
#
# /          |  Positional-Only     |  def func(a, b, /).
# "*"        |  Keyword-Only        |  def func(a, b, *, c).
# /, *       |  Hybrid - Standard   |  def func(a, b, /, c, *, d).
#
# ------------------------------------------------------------------------------------------------

# -> Quando usar cada um no seu código?
#
# 1. Use Positional-Only (/): Em funções matemáticas ou utilitárias muito simples, onde o
# nome do parâmetro é óbvio(ex: dobro(x, /),)
#
# 2. Use Keyword-Only (*): Em quase todas as funções de Backend que possuam "flags" ou 
# configurações(como debug, cache, retry, etc). Isso evita que alguém mude o comporta da
# função acidentalmente ao trocar a ordem dos parâmetros.
#
# 3. Use a combinação (/ e *): Em APIs públicas ou bibliotecas onde você quer garantir
# estabilidade e clareza na interface da função(ex: dados principais da função),
# 
# Exemplo Standard:
#
# def atualizar_pedido(id_pedido, /, status, *, enviar_email=True):
    # id_pedido: Positional-only (O ID é óbvio, não precisa de nome)
    # status: HÍBRIDO (Pode ser por posição ou nome)
    # enviar_email: Keyword-only (Segurança para não confundir com outros booleanos)
#   print(f"Pedido {id_pedido} alterado para {status}. Email enviado: {enviar_email}")
#
# Ambas as chamadas abaixo são válidas para o parâmetro híbrido 'status':
#
# 1. Usando 'status' por posição (mais rápido/curto)
# atualizar_pedido(1025, "Enviado")
#
# 2. Usando 'status' por nome (mais legível/explícito)
# atualizar_pedido(1025, status="Cancelado", enviar_email=False)
#
# ------------------------------------------------------------------------------------------------

# Exemplo Completo com /, standard e *:

def atualizar_pedido(id_pedido, /, status, *, enviar_email=True):
    # id_pedido: Positional-only (O ID é óbvio, não precisa de nome)
    # status: HÍBRIDO (Pode ser por posição ou nome)
    # enviar_email: Keyword-only (Segurança para não confundir com outros booleanos)
    return f"Pedido {id_pedido} alterado para {status}. Email enviado: {enviar_email}"

# Ambas as chamadas abaixo são válidas para o parâmetro híbrido 'status':
#
# 1. Usando 'status' por posição (mais rápido/curto)
print(f"\nExemplo do status do pedido Positional-Only: {atualizar_pedido(1025, 'Enviado')}\n")
#
# 2. Usando 'status' por nome (mais legível/explícito)
print(f"Exemplo do status do pedido Keyword-Only: {atualizar_pedido(1025, status='Cancelado', enviar_email=False)}")

# --- IGNORE ---
#
# Texto da Aula 198
#
# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
# Argumentos entre: / e * são chamados de "Standard Parameters"
# (podem ser posicionais ou nomeados).
#
# Código da Aula:
#
#  def soma(a, b, /, *, c, **kwargs):
#     print(kwargs)
#     print(a + b + c)
#
# soma(1, 2, c=3, nome='teste')