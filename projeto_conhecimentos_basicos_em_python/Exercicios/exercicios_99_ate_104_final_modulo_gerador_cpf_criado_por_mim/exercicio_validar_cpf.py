import exercicio_gerar_cpf_1
import exercicio_gerar_cpf_2
import os
cpf_gerado_pelo_calculo = (
    f"{exercicio_gerar_cpf_1.cpf_limpo[0:9]}"
    f"{exercicio_gerar_cpf_1.resultado}"
    f"{exercicio_gerar_cpf_2.resultado}"
)

cpf_enviado = exercicio_gerar_cpf_1.cpf_limpo
cpf_valido = cpf_gerado_pelo_calculo == cpf_enviado

if len(cpf_enviado) != 11 or cpf_enviado == cpf_enviado[0] * 11:
    os.system("cls")
    print("CPF inválido, muitos números repetidos.")
    exit()

if cpf_valido:
    os.system("cls")
    print(f"{exercicio_gerar_cpf_1.cpf_enviado_cliente} CPF válido")
else:
    os.system("cls")
    print(f"{exercicio_gerar_cpf_1.cpf_enviado_cliente} CPF inválido")

# Esse código é procedural. O que é procedural? E um estilo de programação
# que utiliza funções para resolver problemas.  Nesse estilo, o foco está
# na sequência de ações a serem realizadas para alcançar um objetivo.