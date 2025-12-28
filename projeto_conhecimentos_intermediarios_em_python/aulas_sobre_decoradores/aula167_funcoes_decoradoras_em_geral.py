# Funções Decoradoras e Decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras
# de forma automática em outras funções.


# Sintaxe utilizada para criar funções decoradoras
def inverse_string(original_func):
    def check_type_wrapper(*args, **kwargs):
        result = original_func(*args, **kwargs)
            
        if isinstance(result, str):
            return result[::-1]
        else:
            return str(result)[::-1]
    return check_type_wrapper

@inverse_string
def inverse():
    data_type = input("\nDigite, string ou numbers para inverter: ")
    return data_type

print(f"Result: {inverse()}.")

# Mesma situação decoradora, porém sem @syntax_sugar
print("\nMesma situação decoradora, porém sem @syntax_sugar")
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

def inverte_string(string):
    print(inverte_string.__name__) # Retorna o nome da função que estamos trabalhando
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('1234')
print(invertida)

