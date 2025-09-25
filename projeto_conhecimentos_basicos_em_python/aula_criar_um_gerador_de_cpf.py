import random

# Generador de CPF
for _ in range(100):
    nove_digitos = str(random.randint(100000000, 999999999))

    cpf_limpo = nove_digitos

    soma = 0;
    for i, digito in enumerate(cpf_limpo[:9]):
        peso = 10 - i
        soma += int(digito) * peso

    soma *= 10

    primeiro_digito_verificador = soma % 11

    primeiro_digito_verificador = 0 if primeiro_digito_verificador > 9 else primeiro_digito_verificador

    primeiro_digito = cpf_limpo + str(primeiro_digito_verificador)

    soma2 = 0
    for i, digito in enumerate(primeiro_digito):
        peso2 = 11 - i
        soma2 += int(digito) * peso

    soma *= 10

    segundo_digito_verificador = soma2 % 11

    segundo_digito_verificador = 0 if segundo_digito_verificador > 9 else segundo_digito_verificador

    cpf_gerado_pelo_calculo = f"{nove_digitos}{primeiro_digito_verificador}{segundo_digito_verificador}"

    cpf_formatado = ".".join([cpf_gerado_pelo_calculo[:3], cpf_gerado_pelo_calculo[3:6], cpf_gerado_pelo_calculo[6:9]]) + "-" + cpf_gerado_pelo_calculo[9:]
    print(cpf_formatado)