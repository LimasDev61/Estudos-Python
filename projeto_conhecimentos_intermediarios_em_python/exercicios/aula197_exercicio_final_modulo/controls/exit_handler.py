from assistant import close_datas, clean_screen, list_tasks

repeat = 20 * "-"
def handle_exit(tasks):
    clean_screen()
    if not tasks:
        return close_datas(tasks, option_save = None)
    
    print(f"\n{repeat} Obrigado por usar nosso sistema de tarefas {repeat}\n")

    list_tasks(tasks)

    print("\nVocê deseja salvar suas tarefas? (S/N)\n")

    option_save = input("Escolha a opção desejada: ").strip().upper()

    name = None

    if option_save == "S":
        
        name = input("Digite o nome do arquivo: ").strip()

    return close_datas(tasks, option_save, name_archieve = name)
    