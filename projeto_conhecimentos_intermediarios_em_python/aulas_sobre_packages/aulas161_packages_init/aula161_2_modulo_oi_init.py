def fala_oi(saudacao):
    def oi(nome):
        return f"{saudacao}, {nome}!"
    return oi


# Proteção para evitar mensagens de erro caso o módulo seja importado diretamente
if __name__ == "__main__": # Testando o pacote aulas_packages_init:
    print(fala_oi("Olá")("Maria"))