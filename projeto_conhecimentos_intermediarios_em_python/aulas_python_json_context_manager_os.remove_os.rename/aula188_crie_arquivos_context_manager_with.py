# Criando arquivos com Python + Context Manager with

# O uso do bloco with(Context Manager) é a forma profissional e segura de manipular arquivos
# Ele garante que arquivo seja fechado automaticamente assim que o bloco de código termina,
# mesmo que ocorra um erro dentro do bloco.

# 1. A sintaxe básica
#
# A estrutura subistitui o open() e close() tradicionais.
# sintaxe: with open("caminho_do_arquivo", "modo_de_abertura") as variavel_arquivo:
# variavel_arquivo.write("conteúdo")
# Quando sai do bloco with, o arquivo é fechado automaticamente.

# 2. Os "modos" de Abertura(Flags)
#
# "w" -> Write: Abre para escrita, cria o arquivo se não existir, sobrescreve se existir.
# "a" -> Append: Abre para escrita, cria o arquivo se não existir, adiciona conteúdo ao final 
#  se existir.
# "x" -> Create(Exclusive): Cria o arquivo, retorna um erro(FileExistsError) se o arquivo 
# já existir(evita sobrescrever).
# "r" -> Read: Abre para leitura, retorna um erro(FileNotFoundError) se o arquivo não existir.

# Dica de Ouro: Sempre use ecoding="utf8" ao lidar com texto, especialmente para quem usa
# acentos(ç, ã, é, etc). Isso evita problemas de codificação.

# 3. Porque usar "with", e não o open() tradicional?
#
# É uma questão(boas práticas) de segurança de recursos e prevenção de erros(Stack Overflow).
#
# --- O Jeito "Perigoso"(sem Context Manager):
#
# f = open("teste.txt", "w")
# x = 10 / 0  # Simulando um erro | o programa para aqui sem fechar o arquivo
# f.close() - > Nunca é executado se ocorrer um erro antes
#
# --- O Jeito "Seguro"(com Context Manager):
#
# try:
#     with open("teste.txt", "w") as f:
#         x = 10 / 0 # Simulando um erro | o programa não quebra aqui
# except ZeroDivisionError:
#     print("Erro de divisão por zero capturado! Arquivo foi fechado corretamente.")
#
# O "with" funciona como um bloco try/finally implícito. Ele executa o método especial __exit__
# do objeto do arquivo, que cuida da limpeza, aconteça o que acontecer dentro do bloco.

# ====================================================================
# # RESUMO: SEPARADORES DE CAMINHO DE ARQUIVO (PATH)
# ====================================================================

# 1. BARRA NORMAL ( / )
#    - É o separador universal (Linux, macOS).
#    - Altamente recomendado para portabilidade, pois o Python a aceita
#      e converte corretamente para o separador nativo do sistema (mesmo no Windows).
# Exemplo: caminho = "C:/Users/Usuario/Documentos/arquivo.txt"

# 2. BARRA INVERTIDA DUPLA ( \\ )
#    - É o separador nativo do Windows (\).
#    - Precisa ser duplicada ( \\ ) em strings do Python para evitar que
#      seja interpretada como um caractere de escape (como \n ou \t).
# Exemplo: caminho = "C:\\Users\\Usuario\\Documentos\\arquivo.txt"

# 3. STRINGS RAW ( r"..." )
#    - Alternativa limpa para usar o padrão Windows (\).
#    - O 'r' (raw) desabilita o processamento de caracteres de escape.
# Exemplo: caminho = r"C:\Users\Usuario\Documentos\arquivo.txt"

# DICA ESSENCIAL:
# Para criar caminhos de forma robusta e garantir que o separador correto
# seja usado em qualquer sistema operacional, use sempre os módulos nativos
# do Python como 'pathlib' ou 'os.path.join()'.

# Usei o r"..."(strings raw) para que a barra invertida seja interpretada corretamente
caminho_arquivo = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula188_crie_arquivos_context_manager_with."

# Criando e escrevendo no arquivo usando Context Manager
with open(caminho_arquivo + "txt", "w", encoding="utf8") as arquivo:
    arquivo.write("Arquivo criado com Context Manager!\n")
    arquivo.write("Segunda linha criada com Context Manager!\n")

# closando o arquivo automaticamente ao sair do bloco with