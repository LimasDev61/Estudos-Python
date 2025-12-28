# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Sleep Token - Alkaline
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

from os import system

tarefas = []
desfazer = []

def clear(): 
    system("cls")

print("\nBem-vindo ao seu gerenciador de tarefas!\n")
while(True):
    print("\n-----(Menu Principal)-----\n")
    
    print("1 - Adicionar tarefa")
    print("2 - Desfazer")
    print("3 - Refazer")
    print("4 - Sair")

    print()

    
    # Selecionador de opções
    opcao = input("Escolha a opção desejada: ").strip()

    # Tratamento de erro - para opções inválidas de entrada
    try:
        opcao_number = int(opcao[0:1])
    except (ValueError, IndexError):
        print("\nOpção Inválida, letras não são permitidas!\n")
        print("Lembre-se de escolher uma opção entre 1 e 4!")
        continue
    

    # 4. Encerramento do programa, quando digitamos 4.
    if opcao_number == 4:
        clear()
        if (len(tarefas) > 0):
            print("\nEssas são suas tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i} - {tarefa}")
        else:
            print("\nNenhuma tarefa cadastrada!\n")
        
        print("\nObrigado por usar o gerenciador de tarefas, programa encerrado!\n")
        break
    
    # 1. Adicionar tarefa
    if opcao_number == 1:
        clear()
        print("\n-----(1)Menu: Adicionar Tarefa-----\n")

        print("4 - Sair\n")
        while(True):
            tarefa = input("Digite o nome da tarefa para adicionar: ").strip().capitalize()
            
            if tarefa == "4":
                clear()
                print(f"\nEssas são suas tarefas: {tarefas}\n")
                break
            
            if not tarefa:
                print("\nTarefa vazia, digite novamente!")
                continue

            if tarefa in tarefas:
                print(f"\nErro: A tarefa '{tarefa}' já existe na sua lista!\n")
                continue
            else:
                tarefas.append(tarefa)
                clear()
                print(f"\nA tarefa '{tarefa}' foi adicionada com sucesso!\n")
                print("\nPara sair do menu, digite '4'!\n")

    # 2. Desfazer
    if opcao_number == 2:
        clear()
        print("\n-----(2)Menu: Desfazer-----\n")

        print("4 - Sair\n")
        while(True):
            delete_final = input("\nDigite '2' para desfazer a tarefa final: ").strip()

            if delete_final == "2" and len(tarefas) > 0:
                clear()

                print(f"Essas são suas tarefas atuais:\n")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i} - {tarefa}")
                
                tarefa = tarefas.pop()
                desfazer.append(tarefa)
                print(f"\nA tarefa '{tarefa}' foi desfeita com sucesso!\n")
            else:
                clear()
                print("Aviso:\n")
                print("Você não tem mais tarefas para desfazer, digite '4' para voltar ao menu principal!\n")

            if delete_final == "4":
                clear()
                if len(desfazer) > 0:
                    print("\nEssas são suas tarefas desfeitas:")
                    for i, tarefa in enumerate(desfazer, 1):
                        print(f"{i} - {tarefa}")
                    break
                else:
                    print("\nNenhuma tarefa desfeita!\n")
                    break

    # 3. Refazer
    if opcao_number == 3:
        clear()
        print("\n-----(3)Menu: Refazer-----\n")
        
        print("4 - Sair \n")
        while(True):
            refazer_final = input("\nDigite '3' para refazer a tarefa final: ").strip()

            if refazer_final == "3" and len(desfazer) > 0:
                clear()

                print(f"Essas são suas tarefas desfeitas:\n")
                for i, tarefa in enumerate(desfazer, 1):
                    print(f"{i} - {tarefa}")
                
                tarefa = desfazer.pop()
                tarefas.append(tarefa)
                print(f"\nA tarefa '{tarefa}' foi refeita com sucesso!\n")
            else:
                clear()
                print("Aviso:\n")
                print("Você não tem mais tarefas para refazer, digite '4' para voltar ao menu principal!\n")

            if refazer_final == "4":
                clear()
                if len(tarefas) > 0:
                    print("\nEssas são suas tarefas refeitas:")
                    for i, tarefa in enumerate(tarefas, 1):
                        print(f"{i} - {tarefa}")
                    break
                else:
                    print("\nNenhuma tarefa refazida!\n")
                    break


