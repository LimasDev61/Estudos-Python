# Modos de Abertura de Arquivo e Encoding com with open - Avançado

# Os modos de abertura e o parâmetro encoding, são essenciais para evitar perda de dados
# e erros de acentuação(comuns no Windows).

# Os modos comuns são:
# "r" -> Read: Abre para leitura, retorna um erro(FileNotFoundError) se o arquivo não existir.
# "w" -> Write: Abre para escrita, cria o arquivo se não existir, sobrescreve se existir.
# "a" -> Append: Abre para escrita, cria o arquivo se não existir, adiciona conteúdo ao final 
#  se existir.
# "x" -> Create(Exclusive): Cria o arquivo, retorna um erro(FileExistsError) se o arquivo 
# já existir(evita sobrescrever).

# --------------------------------------------------------------------------------------------
# 1. Os modos avançados(Binário e Atualizações):
#
# "b" -> Binary: Adiciona ao lado dos modos(r,w,a - rb, wb, ab), abre o arquivo no modo binário.
#  - Usados para arquivos que não sejam textos: Imagens, Audios, Vídeos, etc. (binários).
#  - Nota: Não recomendado para arquivos textuais, não usa encoding(bytes puros).
#
# "+" -> Update: Adiciona ao lado dos modos(r,w - r+, w+), abre o arquivo para leitura e escrita.
#  - Usado para atualizar arquivos, evita erros de perda de dados.
#  - "r+" -> Abre a leitura e escrita, retorna um erro(FileNotFoundError) se o arquivo
#     não existir. Não apaga o arquivo, o curso começa no ínicio(sobrescreve o conteúdo);
#  - "w+" -> Abre a leitura e escrita, cria o arquivo se nao existir, sobrescreve se existir e
#     a apaga tudo(igual o w), pouco usado.
#  
# --------------------------------------------------------------------------------------------
# 2. Encoding(O Segredo dos Acentos)
#
# O parâmetro encoding diz ao Python como traduzir bits(0 e 1) para caracteres humanos(a,b, ç, ã).
#
# * Porque é obrigatório definir?
#
# O Windows usa um padrão antigo chamado "cp1252"(ou latin-1) por padrão. 
# O Linux e a Web usam UTF-8 por padrão.
#
# Se criarmos um arquivo no Windows sem definir o encoding e tentar abrir no Linux, ou vice-versa,
# verá caracteres estranhos(O famoso Mojibake).
# - Com encoding, correto: Atenção
# - Sem encoding, incorreto: AtenÃ§Ã£o(Mojibake)
#
# A Regra de Ouro: Sempre, em 100% dos casos de arquivo de texto, use encoding="utf8".
#
# ---------------------------------------------------------------------------------------------
# 4. Exemplos de uso Real
#
# Cenário A: Log de erros("a" - Append) queremos guardar o histórico de erros.
# Exemplo: msg_error = "Erro ao abrir o arquivo"
#
# Cenário B: Configurações Iníciais("x" - Create/Exclusive) queremos criar um arquivo de config,
# mas temos medo de apagar um que o usuário criou.
# exemplo: "theme=dark\nlang=pt-BR\n"
# Erro: Se o arquivo existir, o erro será FileExistsError!
#
# Cenário C: Copia da Imagem("b" -Binário), ler bytes de uma imagem e salvar em outro arquivo(backup).
# Exemplo: imagem.jpg -> backup.jpg.
# obs: Apenas para arquivos que não sejam textos, não usa encoding(bytes puros).
# Erro: Se o arquivo nao for binário, o erro será TypeError: expected string or 
# bytes-like object.
#
# --------------------------------------------------------------------------------------------
# 5. Resumo Para Backend(Data)
#
# Quando formos trabalhar com manipulação de arquivos, .txt é de longe o formato que menos
# usaremos. Mas utilizaremos muito arquivos JSON, XML e CSV.
#
# --------------------------------------------------------------------------------------------

caminho_arquivo_1 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula190.1_modos_de_abertura_de_arquivo_avancado_encoding_with_open."

print("Cenário A - Log de Erros:")

with open(f"{caminho_arquivo_1}txt", "a+", encoding="utf8") as arquivo:
    print("Log de Erros criado com sucesso!")
    arquivo.write("Erro ao abrir o arquivo\n") # cada vez que é chamado, ele adiciona uma nova 
    # linha ao final do arquivo.
    
    print(arquivo.read())


# --------------------------------------------------------------------------------------------
caminho_arquivo_2 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula190.2_modos_de_abertura_de_arquivo_avancado_encoding_with_open."

print("Cenário B - Configurações Iniciais:")

config_padrao = [
    {"theme": "dark", "lang": "pt-BR"},
    {"font": "Arial", "size": 12},
    {"Log": True}
]

try:
    with open(f"{caminho_arquivo_2}config.txt", "x", encoding="utf8") as arquivo:
        for config in config_padrao:
            arquivo.write(f"{config}\n")

except FileExistsError as e:
    print(f"O arquivo {caminho_arquivo_2}config.txt já existe, use 'w' para sobrescrever.\n")

# --------------------------------------------------------------------------------------------
caminho_arquivo_3 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\imagem_aula190_original.png"

print("Cenário C - Cópia da Imagem:")

try:
    with open(f"{caminho_arquivo_3}", "rb") as arquivo:
        with open(f"{caminho_arquivo_3}_backup.png", "wb") as backup:
            for byte in arquivo:
                backup.write(byte)

except TypeError as e:
    print(f"O arquivo {caminho_arquivo_3} não é binário.\n")

print("Imagem copiada com sucesso!", f"\nPath do backup:\n{caminho_arquivo_3}_backup.png\n")

# ---------------------------------------------------------------------------------------------

print("Cenário C Clean - Cópia da Imagem:")

caminho_arquivo_4 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\imagem_aula190_original.png"

try:
    with open(f"{caminho_arquivo_4}", "rb") as arquivo:
        dados = arquivo.read()

    with open(f"{caminho_arquivo_4}_backup.png", "wb") as backup:
        backup.write(dados)

except TypeError as e:
    print(f"O arquivo {caminho_arquivo_4} não é binário.\n")

print("Imagem copiada com sucesso!", f"\nPath do backup:\n{caminho_arquivo_4}_backup.png\n")