# Cuidados com Dados Mutáveis
#................................
# = copia o valor(imutáveis)
# = aponta para o mesmo endereço de memória(mutáveis)

# Mesmo endereço de memória - Imutável
nome = "Renan" # dados imutáveis
nome2 = "Renan" # dados imutáveis
nome3 = "Renan" # dados imutáveis
nome4 = "Renan" # dados imutáveis
nome5 = "Renan" # dados imutáveis

for n in [nome, nome2, nome3, nome4, nome5]:
    print(f"Endereços de Memória:\n{id(n)}")

# Porém, se eu reutilizar a mesma variável com um mesmo nome, ela vai criar um novo endereço de memória
nome = "João"
print(f"\nEndereços de Memória:\n{id(nome)}")

# Com list quando referenciamos ela pra uma nova variavel ela vai apontar para o mesmo endereço de memória - dados mutáveis
lista1 = [1, 2, 3]
lista2 = lista1
print(f"Endereços de Memória:\n{id(lista1)}\n{id(lista2)}")

lista1.append(4)

# Mas caso eu queira copiar uma lista, eu posso usar o .copy(), os endereço de memória serão diferentes
lista2 = lista1.copy()
print(f"Endereços de Memória:\n{id(lista1)}\n{id(lista2)}")