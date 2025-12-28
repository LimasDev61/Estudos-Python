# With Open - Métodos úteis do TextIOWrapper

# O TextIOWrapper é o nome técnico da classe do objeto que o Python cria quando usamos
# a função open() em modo de texto (padrão).
#
# Quando fazemos with open() as f: esse f é uma instância do TextIOWrapper, ele é o
# piloto que traduz os bytes  do disco para as strings que lemos, cuidando do buffer,
# encoding, etc.

# 1. Métodos de Leitura(Extração de Dados)
#
# A diferença entre eles é crucial para a performance e o uso de memória(RAM).
#
# READ(): Lê todo o conteúdo do arquivo na memória de uma vez só e retorna como uma única string.
# pode ser usado com o parâmetro opcional size (ex: size=1, ler 1 byte do arquivo) para limitar 
# a quantidade de caracteres lidos.
#
# Quando usar: Arquivos pequenos, onde o conteúdo completo cabe confortavelmente na memória.
#
# -------------------------------------------------------------------------------------------
#
# READLINE(): Lê o arquivo linha por linha, retornando uma string com a próxima linha a 
# cada chamada.
# Pode ser usado com o parâmetro opcional size (ex: size=10, ler até 10 bytes da linha).
# 
# Quando usar: Arquivos moderados, onde você quer processar uma linha de 
# cada vez(ex: Logs de 5GB).
#
# -------------------------------------------------------------------------------------------
#
# READLINES(): Lê todas as linhas do arquivo e retorna uma lista de strings,
# onde cada string é uma linha do arquivo.
# pode ser usado com o parâmetro size, caso queira limitar a quantidade de blocos de bytes lidos.
#
# Quando usar: Quando precisar iterar ou acessar o arquivo através de índices,
# e o arquivo não for muito grande para caber na memória.
#
# -------------------------------------------------------------------------------------------

# 2. Métodos de Escrita(Inserção de Dados)
#
# WRITE(): Escreve uma string no arquivo na posição atual do cursor(ponteiro, ex: 0).
# Retorna o número de caracteres escritos.
#
# Quando usar: Sempre que precisar escrever ou sobrescrever conteúdo no arquivo.
#
# Obs: Para ver a posição do cursor: f.tell() mostra em que bytes estou escrevendo.
#
# -------------------------------------------------------------------------------------------
# 
# WRITELINES(): Escreve uma lista de strings no arquivo, sem adicionar quebras de linha(\n)
# automaticamente. Cada string da lista é escrita sequencialmente.
#
# Quando usar: Quando precisar escrever múltiplas linhas de uma vez,
# mas lembre-se de adicionar as quebras de linha manualmente.
# Utilize uma compreensão de lista para adicionar \n ou map antes de passar a lista.
# Exemplo: linhas = [f"Linha {i}\n" for i in range(5)]
# f.writelines(linhas)
# Ou: f.writelines(map(lambda x: x + "\n", linhas))
#
# -------------------------------------------------------------------------------------------

# 3. Métodos de Navegação do Cursor
#
# TELL(): Retorna a posição atual do cursor(ponteiro) no arquivo, em bytes.
# Útil para saber onde você está lendo ou escrevendo no arquivo.
#
# Quando usar: Sempre que precisar monitorar ou registrar a posição do cursor.
#
# -------------------------------------------------------------------------------------------
#
# SEEK(offset(ex: 10), whence=0(from, 0(from atual), 2(from fim)): Move o cursor 
# para uma nova posição no arquivo.
#
# Quando usar: Quando precisar navegar ou modificar a posição do cursor.
#
# offset -> Quantidade de bytes a serem movidos.
# whence -> Origem da nova posição do cursor. 0(from atual), 1(from inicio), 2(from fim).
#
# Exemplo 1: f.seek(10, 0) ou f.seek(10)
# Ação: Define o ponteiro na posição 10 bytes a partir do início.
# Resultado: O ponteiro fica no 11º byte (contagem começa em 0).
# 
# Exemplo 2: f.seek(-5, 2)
# Ação: Move o ponteiro 5 bytes para trás (negativo) a partir do final do arquivo.
# Resultado: O ponteiro fica na posição 45.
# 
# Exemplo 3: f.seek(5, 1) - Não funciona em modo Texto(UTF8)
# (Assumindo que o ponteiro está em 20)
# Ação: Move o ponteiro 5 bytes para frente (positivo) a 
# partir da posição atual (20).
# Resultado: O ponteiro fica na posição 20 + 5 = 25.
#
# -------------------------------------------------------------------------------------------

# 4. Gerenciamento de Buffer(flush)
#
# Quando demos um write(), o Python não grava no disco imediatemente. Ele guarda num buffer
# na memória para economizar acesso ao disco(que é lento). O Python só grava quando o buffer
# enche ou quando o arquivo fecha.
#
# - flush(): O Python é forçado a despejar o buffer no disco agora, sem fechar o arquivo.
#
# - Uso no Backend: Em sistemas de log em tempo real, se o sistema travar antes de fechar o
# arquivo, você perde o que estava no buffer. Então, use flush() para garantir que o buffer
# seja escrito antes de fechar o arquivo.
#
# -------------------------------------------------------------------------------------------

# 5. Propriedades Úteis(Atributos)
#
# Não são métodos(não contém parênteses), são informações de objetos.
#
# vamos usar o exemplo do alias do arquivo(f):
#
# f.close: Booleano(True se o arquivo fechou)
# f.mode: Qual modo foi usado(ex: r, w, a, r+, w+, a+)
# f.name: O caminho/nome do arquivo
# f.encoding: O encoding usado(ex: utf-8)
# f.errors: O modo de tratamento de erros(ex: ignore, strict, replace)
# f.buffer: O buffer do arquivo
#
# -> Resumo Para Roadmap(Backend/Data)
#
# 1. Use for linha in arquivo: Para ler dados grandes de um arquivo.
# 2. Use seek(0) se precisar ler o arquivo novamente.
# 3. Use tell() para saber onde estou lendo(bytes).
# 4. Use flush() para garantir que o buffer seja escrito antes de fechar o arquivo, como
# logos críticos que não podem ser perdidos em um crash(travamento do sistema).
#
# -------------------------------------------------------------------------------------------

# obs: sempre use txt ao criar o arquivo de texto:
# Exemplo_1: caminho_arquivo + "txt"
# Exemplo_2: caminho_arquivo + ".txt"
# Exemplo_3: f"{caminho_arquivo}txt" ou f"{caminho_arquivo}.txt"

# 1. ---------------------------------------------------------------------------------------

caminho_arquivo_1 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula189.1_with_open_metodos_uteis_do_textiowrapper."

# Podemos também criar um arquivo em branco no caminho escolhido:
# f = open(f"{caminho_arquivo_1}txt", "w", encoding="utf8") as arquivo:
# ...

def separador():
    print("-" * 10)
    print()

with open(f"{caminho_arquivo_1}txt", "w", encoding="utf8") as arquivo:
    print("\nTipo de objeto do arquivo:", type(arquivo).__name__)
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    arquivo.write("Linha 4\n")
    arquivo.write("Linha 5\n")

print("\n1. Metodos de Leitura(Extração de Dados)\n")
# obs: "w+" abre o arquivo para leitura e escrita
# nome do arquivo: aula189.1

# Exemplo 1 - read() - ler o conteúdo do arquivo
# pode se o usar o parâmetro size
print("Exemplo 1 - read():")
with open(f"{caminho_arquivo_1}txt", "r", encoding="utf8") as arquivo:
    print(arquivo.read(1)) # size=1 byte, ler, apenas o primeiro caractere
    print(arquivo.read()) # Ler todo o conteudo do arquivo

separador()
# Exemplo 2 - readline() - Ler apenas uma linha até encontra o \n
# pode se o usar o parâmetro size
print("Exemplo 2 - readline():")
with open(f"{caminho_arquivo_1}txt", "r", encoding="utf8") as arquivo:
    print(arquivo.readline())

separador()
# Exemplo 3 - readlines() - Ler todas as linhas do arquivo, transformando em uma lista
# pode se o usar o parâmetro size
print("Exemplo 3 - readlines():")
with open(f"{caminho_arquivo_1}txt", "r", encoding="utf8") as arquivo:
    print(arquivo.readlines()) 

# Exemplo 4 - readlines() - Ler todas as linhas do arquivo, transformando em uma lista
# pode se o usar o parâmetro size
print("Exemplo 4 - readlines() com for:")
with open(f"{caminho_arquivo_1}txt", "r", encoding="utf8") as arquivo:
    for linha in arquivo:
        print(linha, end="")

# 2. ---------------------------------------------------------------------------------------

separador()
print("\n2. Métodos de Escrita(Gravação)\n")
# Verifique na pasta caminho para ver as modificações feitas entre os exemplos
# nome do arquivo: aula189.2
caminho_arquivo_2 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula189.2_with_open_metodos_uteis_do_textiowrapper."

print("write() - Escreve uma string na Posição atual do Cursor.\n")
print("writelines() - Escreve uma lista de strings no arquivo, sem adicionar quebras de linha " \
        "automáticamente.")

# Exemplo 1 - Write() - Escreve uma string na Posição atual do Cursor
with open(f"{caminho_arquivo_2}txt", "w", encoding="utf8") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    arquivo.write("Linha 4\n")
    arquivo.write("Linha 5\n")

# Exemplo 2 - Writelines() - Escreve uma lista de strings no arquivo
# não adiciona quebras de linha automaticamente (\n).

# Com o Writelines(), apesar dele não adicionar quebra de linhas ao final, podemos fazer
# de dois jeitos para acrescentar a quebra de linhas:
# 1º Exemplo: linhas = ["Linha 1\n", "Linha 2\n", "Linha 3\n", "Linha 4\n", "Linha 5\n"]
# 
# 2º Exemplo(recomendado - listcomprehension): arquivo.writelines[f"{nome}\n" for nome in nomes]

# Exemplo(Jeito Incorreto): Vai gerar um nome colado na linha seguinte
# linhas = ["Linha 1", "Linha 2", "Linha 3", "Linha 4", "Linha 5"]
# with open(f"{caminho_arquivo_2}txt", "w", encoding="utf8") as arquivo:
#    arquivo.writelines(linhas)

# Exemplo(Jeito Correto): Vai gerar um nome colado na linha seguinte
linhas = [f"Linha {i}\n" for i in range(5)]
with open(f"{caminho_arquivo_2}txt", "w", encoding="utf8") as arquivo:
    arquivo.writelines(linhas)

# 3. ---------------------------------------------------------------------------------------

separador()
print("3. Métodos de Navegação(Manipulação/Posição de Cursor)\n")
# nome do arquivo: aula189.3
caminho_arquivo_3 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula189.3_with_open_metodos_uteis_do_textiowrapper."

with open(f"{caminho_arquivo_3}txt", "w+", encoding="utf8") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    arquivo.writelines(("linha 4\n", "linha 5\n"))

    arquivo.seek(0, 0)
    print(arquivo.read())
    print("Posição final do cursor: ", arquivo.tell())

    print("\nLendo...\n")
    
    arquivo.seek(0, 0) # Ler a parti do byte 0, posição 0
    print(arquivo.readline()) 
    print(arquivo.readline(), end="") # end='' para remover os espaços em branco, após \n.
    print(arquivo.readline().strip()) # strip() para remover os espaços em branco, após \n.
    print(arquivo.readline().strip()) 
    print("Posição atual do cursor(Pós-leitura): ", arquivo.tell())

    print("\nLeitura READLINES com FOR:")
    arquivo.seek(0)
    for linha in arquivo.readlines():
        print(linha.strip())

    
# 4. ---------------------------------------------------------------------------------------

separador()
print("4. Gerenciamento de Buffer(flush)\n")
# obs: "w+" abre o arquivo para leitura e escrita
# nome do arquivo: aula189.4
caminho_arquivo_4 = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula189.4_with_open_metodos_uteis_do_textiowrapper."

print("Para maiores informações sobre o FLUSH, verifique no ínicio desse código.")
with open(f"{caminho_arquivo_4}txt", "w+", encoding="utf8") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    arquivo.write("Linha 4\n")
    arquivo.write("Linha 5\n")
    
    arquivo.flush()
    
# 5. ---------------------------------------------------------------------------------------

separador()
print("5. Propriedades Úteis(Atributos)\n")

print("Para maiores informações sobre as propriedades úteis(atributos)", \
    "verifique no ínicio desse código.")
