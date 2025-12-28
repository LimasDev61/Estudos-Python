# Evitando o uso de Condicionais + Guard Clause

# Apesar de se tratar de funções que fazem o tratamento objetivo de erro ou exceção, separei 
# esse tópico das aulas de funções para que fosse mais clara a explicação.

# Essa é uma das técnicas mais eficazes transformar um código "macarrônico" em um código 
# limpo, legível e de fácil manutenção. O uso do Guard Clause(Clausula de Guarda) visa
# eliminar o aninhamento excessivo de if e else(o famoso código pirâmide).

# A ideia é simples: Verificar as condições de erro ou excções primeiro e saida da função
# o quanto antes.

# 1. O Problema: Código Pirâmide(Nested ifs)
#
# Neste estilo, o caminho feliz(a lógica principal) fica escondido no fundo de vários níveis
# de identação.
#
# Exemplo:
#
# def processar_pagamento(usaurio, valor):
#     if usuario.esta_ativo():
#         if valor > 0:
#             if usuario.tem_saldo(valor):
#                 # A lógica principal(Caminho Feliz)
#                 usuario.deduzir_saldo(valor)
#                 return "Sucesso"
#             else:
#                 return "Saldo insuficiente"
#         else:
#             return "Valor inválido"
#     else:
#         return "Usuário inativo"
#
#
# * Principais problemas do Nested ifs:
# - Dificuldade de manutenção
# - Dificuldade de entendimento
# - Dificuldade de depuração
# - Redução de carga cognitiva do desenvolvedor
# - Redução de legibilidade do código(código sujo)

# 2. Solução: Guard Clause(Clausula de Guarda)
#
# Invertemos a lógica: Tratamos os problemas primeiro com um return imediato. O "caminho feliz"
# fica na raiz da função(sem identação extra).
#
# Exemplo:
#

from os import system

# Limpa o terminal
def clear(): 
    system("cls")


# Valida a Entrada.
def validar_entrada(entrada):
    try:
        entrada = int(entrada)
    except (TypeError, ValueError):
        clear()
        raise TypeError("\nEntrada inválida, digite novamente com valores numéricos!")

    if entrada < 1 or entrada > 4:
        clear()
        raise IndexError("\nDigite uma opção entre 1 e 4!")

    return entrada


# Lista as tarefas do usuário
def listar_tarefas(tarefas):
    clear()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada!\n")
        return

    print("\nEssas são suas tarefas:\n")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i} - {tarefa}")


# 4. Sair do Sistema
def exit_sector(tarefas):
    clear()

    if not tarefas:
        print("\nVocê saiu do Gerenciador de Tarefas sem tarefas!\n")
        exit()
        

    print("\nEssas são suas tarefas:\n")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i} - {tarefa}")

    print("\nObrigado por usar nosso gerenciador de tarefas!")

    exit()


# 1. Adicionar Tarefa - Guard Clause
def adicionar_tarefa(texto_tarefa, lista_original):

    tarefa_formatada = texto_tarefa.strip().capitalize()

    if not tarefa_formatada:
        return "\nVocê não digitou uma tarefa, digite novamente!"
        
    
    if tarefa_formatada in lista_original:
        return f"\nErro: A tarefa '{tarefa_formatada}' já existe na sua lista!\n"
        
    
    lista_original.append(tarefa_formatada)

    return f"\nA tarefa '{tarefa_formatada}' foi adicionada com sucesso!\n"

# 2. Desfazer Tarefa - Guard Clause
def desfazer_tarefa(tarefas, desfazer_tarefa):
    clear()

    print("\n-----(2 - Desfazer Tarefa)-----\n")
    
    if not tarefas:
        return "\nNão há tarefas para desfazer!"
    
    tarefa = tarefas.pop()
    desfazer_tarefa.append(tarefa)

    return f"\nA tarefa '{tarefa}' foi desfeita com sucesso!\n"
    
# 3. Refazer Tarefa - Guard Clause
def refazer_tarefa(tarefas, refazer_tarefa):
    clear()
    
    print("\n-----(3 - Refazer Tarefa)-----\n")

    if not refazer_tarefa:
        return "\nNão há tarefas para refazer!"
    
    tarefa = refazer_tarefa.pop()
    tarefas.append(tarefa)

    return f"\nA tarefa '{tarefa}' foi refeita com sucesso!\n"

# 4. Dispatch Table
def dispatch_table(opcao, tarefas, desfazer):
    
    opcoes = {
        1: lambda: f"\nTarefas foram adicionadas com sucesso.",
        2: lambda: desfazer_tarefa(tarefas, desfazer),
        3: lambda: refazer_tarefa(tarefas, desfazer),
        4: lambda: exit_sector(tarefas)
    }
    resultado = opcoes.get(opcao, lambda: None)
    return resultado()

    


tarefas = []
desfazer = []

print("\nBem-vindo ao Gerenciador de Tarefas!\n")
while True:

    print("\n-----(Menu Principal)-----\n")
    print("1 - Adicionar tarefa")
    print("2 - Desfazer")
    print("3 - Refazer")
    print("4 - Sair\n")

    opcao_escolha = input("Escolha a opção desejada: ").strip()

    try:
        opcao_validada = validar_entrada(opcao_escolha)

        tarefas_nomes = None

        if opcao_validada == 1:
            print("\n-----(1 - Adicionar Tarefa)-----\n")

            print("4 - Salvar as Tarefas e Sair")
            while True:

                tarefas_nomes = input("\nDigite o nome da tarefa: ")

                if tarefas_nomes == "4":
                    clear()

                    print()

                    listar_tarefas(tarefas)
                    break
                
                salvar_tarefa = adicionar_tarefa(tarefas_nomes, tarefas)

                print(salvar_tarefa)

                continue

                

        sucesso = dispatch_table(opcao_validada, tarefas, desfazer)
        if sucesso:
            print(sucesso)

    except (TypeError, IndexError) as e:
        print(e)
        continue
    

# 3. Vantagens de usar Guard Clauses
#
# 1. Redução de carga cognitiva: Você não prcisa manter na cabeça 4 condições if para entender
# o que acontece no final do programa..
#
# 2. Facilidade de teste: Cada clásula de guarda é um caso de teste claro e isolado.
#
# 3. Linearidade: O código é lido de cima para baixo como uma lista de Requesitos.
#
# 4. Redução de depuração: Os erros são encontrados na clásula de guarda mais prática.
#
# 5. Aumento de legibilidade: O código fica mais claro e legível.