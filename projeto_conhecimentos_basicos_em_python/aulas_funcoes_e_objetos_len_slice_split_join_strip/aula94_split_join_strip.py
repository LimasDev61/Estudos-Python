# Split e Join com list e str
# Split - Divide uma String
# Join - Une a String
# strip - Retira Espaços o inicio e fim de uma string, assim como retira dados sujos.

# Exemplo - Split
frase = "Eu sou fã do Python, para sempre!"

transformar_frase_list = frase.split()
caractere_como_parametro = frase.split(",") # vai quebrar na virgula.

print(transformar_frase_list)
print(caractere_como_parametro)

# Exemplo - Join
lista = ["Eu", "sou", "fã", "do", "Python", "para", "sempre!"]
frase_sem_espaco = "".join(lista) # tirando os espaços
frase_com_espaco = " ".join(lista) # colocando os espaços
frase_com_separador = "-".join(lista)

print(frase_sem_espaco)
print(frase_com_espaco)
print(frase_com_separador)

# Exemplo - Strip
frases = "   Eu sou fã do Python, para sempre!   "
frase_sem_espaco = frases.strip() # tirando os espaços
frase_sem_espaco_esquerda = frases.lstrip() # tirando os espaços da esquerda
frase_sem_espaco_direita = frases.rstrip() # tirando os espaços da direita

print(frase_sem_espaco)
print(frase_sem_espaco_esquerda)
print(frase_sem_espaco_direita)

# Exemplo - Split e Join no For

print("\nExemplo - Split e Join no For")
frase2 = "   Eu sou fã     do   Python,  para  sempre!   "
print(frase2)
frases_sem_espaco = []

for frase in frase2.split():
    frases_sem_espaco.append(frase.strip())

print(frases_sem_espaco)

transformar_em_frase_comum = " ".join(frases_sem_espaco)

print(transformar_em_frase_comum)