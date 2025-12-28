from controls.start_control import start_options
from os import system

tarefas = []
desfazer = []

print("\nBem-vindo ao Gerenciador de Tarefas!")
while True:

    print("\n-----(Menu Principal)-----\n")
    print("1 - Adicionar tarefa")
    print("2 - Desfazer")
    print("3 - Refazer")
    print("4 - Sair\n")

    opcao = input("Escolha a opção desejada: ").strip()

    try: 
        if opcao == "1":
            system("cls")
            print("\n-----(1) Menu: Adicionar Tarefa-----\n")

            while True:
                nome_tarefa = input("Digite o nome da tarefa para adicionar: ")

                if nome_tarefa == "4":
                    system("cls")
                    print("-> Você saiu do menu - Adicionar Tarefa.\n")
                    break

                sucesso = start_options(opcao, tarefas, desfazer, nome_tarefa)

        elif opcao in ["2", "3", "4"]:
            resultado = start_options(opcao, tarefas, desfazer, nome_tarefa)

    except Exception as e:
        print(f"\nErro: {e}\n")