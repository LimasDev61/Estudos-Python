# Manipulando chaves e valores em um dicionário
# Adicionando, atualizando, removendo e verificando

pessoa = {
    "nome": "Renan",
    "sobrenome": "Lima",
    "idade": 33,
    "altura": 1.69,
    "enderecos": [
        {"rua": 16, "setor": "Oeste", "número": 123},
        {"rua": 25, "setor": "Sul", "número": 321},
    ]
}

# Adicionando
pessoa["peso"] = 70
print(pessoa)

# Atualizando
pessoa["peso"] = 72
print(pessoa)

# Removendo
del pessoa["altura"]
print(pessoa)

# Verifiando os endereços
print(pessoa["enderecos"])
for endereco in pessoa["enderecos"]:
    print(endereco)
    for chave in endereco:
        print(f"{chave}: {endereco[chave]}")
    print()