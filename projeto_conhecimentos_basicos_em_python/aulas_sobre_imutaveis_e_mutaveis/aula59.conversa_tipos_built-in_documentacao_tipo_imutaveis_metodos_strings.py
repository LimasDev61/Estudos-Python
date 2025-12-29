"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = '1000'
outra_variavel = f'{string[:3]}ABC{string[4:]}'

print("\nÉ uma string, tipo str que é imutável:", string)

print("\noutra_variavel, para concatenar os valores imutáveis:", outra_variavel)

print("\nzfill, para preencher com zeros a esquerda, built-in:", (string.zfill(10)))

# Tipos imutáveis não são alterados, apenas criamos novos objetos na memória com as alterações desejadas.
# os dados antigos permanecem inalterados.