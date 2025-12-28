# Salvando Dados Python em JSON com Módulo json

# O JSON(JavaScript Object Notation) é o formado de dados mais utilizado para comunicação
# entre sistemas(APIs, Banco de Dados, etc) e para salvar configurações em arquivos web ou
# backend.

# O módulo nativo json do Python, transforma objetos Python(dicionários, listas, etc) em 
# textos JSON e vice-versa.

# 1. Mapeamento de Python <-> JSON
#
# É importante saber como os tipos de dados são traduzidos:
#
# Python                          ->  JSON
# dict(dicionary)                 ->  Object {}
# list, tuple(tuplas e listas)    ->  Array []
# str(string)                     ->  String ""
# int, float(números)             ->  Number(Números)
# True                            ->  true
# False                           ->  false
# None                            ->  null
#
# --------------------------------------------------------------------------
# 2. Salvando(Escrevendo) Dados em JSON(json.dump)
#
# Para salvar um dicionário o Python em um arquivo, usamos a função json.dump().
#
# A forma mais segura e comum é combiná-la com o Context Manager(with open).
#
# --------------------------------------------------------------------------
# 3. Parâmetros Importantes
#
# - ensure_ascii = False: Crucial! Sem este parâmetro, o Python transforma caracteres como "ã"
# e "ç" em sequências de escape("\u00c7" e "\u00e3"). Ao usar FALSE, o JSON fica legível para
# humanos. (Porém, trabalhando em produção, podemos utiliza-lo assim para evitar problemas de
# compatibilidade com o JSON).
#
# - indent = 4: Adiciona quebra de linha e 4 espaços para identação. Isso não é obrigatório para
# maquinas, mas torna o arquivo JSON bonito e fácil de ser interpretado. 
#
# --------------------------------------------------------------------------
# 4. Carregando(Lendo) Dados de JSON(json.load)
#
# Para ler dados de um arquivo JSON e transformá-lo de volta em um dicionário Python, usamos
# a função json.load().
#
# A forma mais segura e comum é combiná-la com o Context Manager(with open).
#
# --------------------------------------------------------------------------
# 5. Bonus: Strings JSON(json.dumps e json.loads)
#
# As vezes não estamos lidando com arquivos, mas sim com string de texto que veio de uma API(ex:
# a biblioteca requests).
#
# Para transformar uma string JSON em um dicionário Python, usamos json.loads().
# Para transformar uma string Python em uma string JSON, usamos json.dumps().
#
# --------------------------------------------------------------------------

import json

pessoa = {
    "nome" : "Renan",
    "sobrenome" : "Lima",
    "idade" : 33,
    "enderecos" :[
        {"rua" : 20, "numero": 123},
        {"rua" : 30, "numero": 321},
    ],
    "altura" : 1.69,
    "numeros_favoritos" : (1, 8, 33),
    "dev" : True,
    "linguagem_favorita" : "Python",
    "cpf" : None,
}

# print("\nSalvando arquivo em JSON:")
caminho_arquivo = r"C:\Users\USUARIO1\Documents\Python - Learning\python_estudos_contextmanager\aula192.1_arquivo_json"
variavel_json = f"{caminho_arquivo}.json"

# with open(variavel_json, "w", encoding="utf8") as arquivo:
#    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

# print("Arquivo salvo com sucesso!")

# print("\nConvertendo JSON em Python:")
# with open(variavel_json, "r", encoding="utf8") as arquivo:
#    pessoa_json = json.load(arquivo)
#    print(pessoa_json)
#    print(type(pessoa_json))

# print("\nConvertendo uma string em JSON:")
# string_json = json.dumps(pessoa, ensure_ascii=False, indent=4)
# print(string_json)
# print(type(string_json))

print("\nConvertendo uma string em Python:")
# """ = docstrings
string_json = """{
    "nome": "Renan",
    "sobrenome": "Lima",
    "idade": 33,
    "enderecos": [
        {
            "rua": 20,
            "numero": 123
        },
        {
            "rua": 30,
            "numero": 321
        }
    ],
    "altura": 1.69,
    "numeros_favoritos": [
        1,
        8,
        33
    ],
    "dev": true,
    "linguagem_favorita": "Python",
    "cpf": null
}"""
pessoa_json = json.loads(string_json)
print(pessoa_json)
print(type(pessoa_json))

print("\nExibindo os dados do dicionário em string Python:")
for key, value in pessoa_json.items():
    print((f" - {key}: {value}"))