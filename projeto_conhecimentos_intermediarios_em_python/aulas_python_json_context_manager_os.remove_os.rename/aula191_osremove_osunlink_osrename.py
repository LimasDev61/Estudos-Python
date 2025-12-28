import os
# os.remove, os.unlink e os.rename - apagando, renomeando e movendo arquivos

# Funções do módulo os, são essenciais para trabalhar com arquivos e pastas
# do sistema operacional.

# 1. Apagando Arquivos(os.remove, os.unlink)
#
# Ambas as funções fazem exatamente a mesma coisa - apagar um arquivo do disco.
#
# - os.remove(caminho): É o nome mais amigável e comum em scripts Python(especialmente no 
#   Windows).
#
# - os.unlink(caminho): É o nome tradicional do mundo Unix/Linux. Tecnicamente, ele remove
#   o link simbólico, de um arquivo ou diretório, mas ele tem o mesmo efeito.
#
# Atenção! 
#
# 1. Elas não apagam pastas(diretórios). Se tentar, receberá um IsADirectoryError. Para pastas
#   use-se os.rmdir().
#
# 2. A exclusão é permanente. O arquivo ou diretório não pode ser recuperado da lixeira.
#
# --------------------------------------------------------------------------------------------
#
# 2. Renomeando e Movendo(os.rename)
#
# No nível do sistema operacional, renomear e mover(dentro do disco) são as mesmas operações:
# podemos apenas alterar o caminho(path) ou o nome do arquivo.
#
# A. Para renomear(Mesma Pasta):
# Muda apenas o nome, mantém na mesma pasta.
# os.rename("relatorio_2024.txt", "relatorio_2025.txt")
#
# B. Para mover(Troca de Pasta - Cut & Paste):
# Se alterarmos o diretório no caminho do destino o arquivo é movido.
#
# Move pasta "downloads" para a pasta "documentos".
# Importante: A pasta destino do "documentos", já deve existir.
# os.rename(caminho_antigo, caminho_novo)
#
# Atenção! 
#
# O os.rename funciona bem para mover arquivos dentro da mesma partição(ex: tudo dentro do C:).
# Se tentarmos mover do C: para um PenDriver(D:), o os.rename pode falhar dependendo da versão
# do Python e do sistema operacional. Para mover entre discos diferentes, é mais seguro usar
# a biblioteca shutil.
#
# --------------------------------------------------------------------------------------------
#
# 3. A Alternativa Moderna(pathlib)
#
# Como estamos aprendendo as melhores práticas atuais(Python 3+), a biblioteca "os" é
# considerada "baixo nível". A forma moderna e orientada a objetos é usar o pathlib.
#
# Resumo Rápido:
#
# os.remove/os.unlink -> path.unlink() - apaga arquivos
# os.rename -> path.rename() - renomeia/move arquivos
# os.path.join -> renomeia ou move para outra pasta
# os.rmdir -> path.rmdir() - apaga pastas(diretórios)
#
# --------------------------------------------------------------------------------------------
#
# 4. Sobre o shutil
#
# Resumo Breve:
# O Módulo shutil(Shell Utilities) é o "irmão forte" do "os". Enquanto "os" lida com operações
# básicas de baixo nível, o shutil é projetado para operações de alto nível, como copiar arquivos(copy),
# arquivar, copiar metadados de arquivos(copy2), copiar arquivos e pastar entre discos(C: -> D:)
# e limpeza nuclear, responsável por apagar diretórios inteiros de arquivos(shutil.rmtree()).
#
# Resumo Comparativo(os vs shutil)
#
# - Apagar Arquivos: os.remove() ideal para arquivos soltos, melhor que o shutil que apaga tudo.
# - Apagar Pastas: os.rmdir(), apaga apenas pastas vazias -> shutil.rmtree() apaga tudo dentro de uma pasta.
# - Renomear/Mover: os.rename, move arquivos só no mesmo disco -> shutil.move() move arquivos 
# - com segurança entre discos.
# - Copiar arquivos:
#   - os -> não copia arquivos.
#   - shutil -> shutil.copy() copia arquivos sem metadados. 
#            -> shutil.copy2() copia arquivos com metadados(ex: data de modificação).
#            -> shutil.copytree() copia todos os arquivos e pastas com metadados.
#
# --------------------------------------------------------------------------------------------

# Bônus 1: Criando Zips(make_archive)
#
# - shutil.make_archive() cria arquivos zip.
# - shutil.unpack_archive() descompacta arquivos zip.
#
# Para maiores informações, verifique a documentação oficial: 
# https://docs.python.org/3/library/shutil.html
#
# Bonus 2: os.path - modo legado!
#
# - os.path.join() - junta caminhos de arquivos.
# - os.path.split() - divide o caminho em duas partes: caminho e nome do arquivo.
# - os.path.isdir() - verifica se o caminho é uma pasta.
# - os.path.isfile() - verifica se o caminho é um arquivo.
# - os.path.exists() - verifica se o caminho existe.
# - os.path.dirname() - retorna o caminho da pasta.
# - os.path.basename() - retorna o nome do arquivo(diretamente no caminho).
#
# --------------------------------------------------------------------------------------------

caminho_arquivo_1 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula191.1_arquivo_de_log_de_erros"

print("\nMétodos: os.remove, os.unlink - remover arquivos:\n")
with open(f"{caminho_arquivo_1}.txt", "w", encoding="utf8") as arquivo:
    print("Arquivo Criado -> Log de Erros criado com sucesso!\n")
    arquivo.write("Erro ao abrir o arquivo\n")


print(f"Removendo o arquivo -> {caminho_arquivo_1} | com os.remove:")
os.remove(f"{caminho_arquivo_1}.txt")
print("Arquivo de Log de Erros - removido com sucesso!\n")

# ideal para Unix e Linux
#print("Removendo o arquivo com os.unlink:")
#os.unlink(f"{caminho_arquivo_1}.txt")
#print("Arquivo removido com sucesso!\n")

print(40 * "-")
print("Método: os.rename - renomear/mover arquivos:\n")

arquivo_1_principal = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula191_relatorio_de_erros_2024"
arquivo_1_renomeado = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula191_relatorio_de_erros_2025"

arquivo_principal = f"{arquivo_1_principal}.txt"
arquivo_renomeado = f"{arquivo_1_renomeado}.txt"

with open(arquivo_principal, "w", encoding="utf8") as arquivo:
    print("Arquivo Criado -> Log de Erros criado com sucesso!\n")
    arquivo.write("Erro ao abrir o arquivo\n")

print("Renomeando o arquivo aula191_relatorio_de_erros_2024 -> aula191_relatorio_de_erros_2025:")
try:
    os.rename(arquivo_principal, arquivo_renomeado)
    print("Arquivo renomeado com sucesso!\n")
except FileExistsError:
    print("O arquivo já foi criado!\n")


print(40 * "-")
caminho_do_backup = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula191_pasta_para_mover_arquivos\aula191_relatorio_de_erros_2025"

print("Movendo o arquivo relatorio_de_erros_2025 -> pasta aula191_pasta_para_mover_arquivos:")
os.rename(arquivo_renomeado, caminho_do_backup)
print("Arquivo movido com sucesso!\n")


