# Decoradores são @Syntax_Sugar para criar funções decoradoras
# Tradução - @Syntax_Sugar: Açúcar Sintático 
def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f"O seu resultado foi {resultado}.")
        print("Ok, agora você foi decorada")
        return resultado
    return interna

@criar_funcao # Syntax Sugar
def inverte_string(string):
    print(inverte_string.__name__) # Retorna o nome da função que foi sobrescrito pelo wrapper do decorador
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")

# O decorador da função inverte_string_checando_parametro
# inverte_string_checando_parametro = criar_funcao(inverte_string)
# é substituido pelo Syntax Sugar @criar_funcao - Cria um atalho para uma função
invertida = inverte_string("1234")
print(invertida)
