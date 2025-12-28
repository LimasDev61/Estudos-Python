# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados em matemática e são coleções não ordenadas de elementos únicos.
# https://brasilescola.uol.com.br/matematica/conjunto.html
# Representados graficamente por diagramas de Venn
# https://pt.wikipedia.org/wiki/Diagrama_de_Venn
# Sets em Python são mutáveis, mas seus elementos devem ser imutáveis (números, strings, tuplas).

# Criando um set
# set(iteraveis) ou {elementos, separados, por, vírgula}
# Não existe set vazio com {}, isso cria um dicionário vazio
s1 = {"Renan", 1, 2, 3} # set com elementos
print(type(s1))  # Saída: <class 'set'>
print(s1)        # Saída: {'Renan', 1, 2, 3} (ordem pode variar)
s2 = set("Renan")  # set vazio - construtor set() vai por iteráveis quando se tem strings
print(type(s2))  # Saída: <class 'set'>
print(s2)        # Saída: {'R', 'e', 'n', 'a'} (ordem pode variar, letras repetidas são removidas)

# Sets são eficientes para remover valores duplicados de iteráveis
# - eles não tem index;
# - eles não garantem ordem;
# eles são iteráveis e podem ser percorridos com loops (for, in, not in);

# Tirar itens repetivos de uma lista
lista = [1, 2, 3, 4, 5, 1, 2, 3]
print(lista)  # Saída: [1, 2, 3, 4, 5, 1, 2, 3]
lista = list(set(lista))  # Converte a lista para set e volta para lista
print(lista)  # Saída: [1, 2, 3, 4, 5] (ordem pode variar)

s4 = {"Renan", 1, 2, 3, (4, 5,)}  # 
print(s4)  # Saída: {'Renan', 1, 2, 3, (4, 5)} (ordem pode variar)