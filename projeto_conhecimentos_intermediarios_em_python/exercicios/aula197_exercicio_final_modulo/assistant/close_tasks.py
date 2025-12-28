from .clear_console import clean_screen
from .list_task import list_tasks
from .save_task import save_data

def close_datas(tasks, option_save, name_archieve = None):
    clean_screen()
    
    if not tasks:
        print("\nNenhuma tarefa cadastrada, obrigado por usar o nosso sistema.\n")
        return True
    
    list_tasks(tasks)
    
    if option_save == "S":
        if name_archieve:
            save_data(tasks, name_archieve)
            print("\nTarefas salvas com sucesso.")
            print("obrigado por usar nosso sistema.")
            exit()
        else:
            print("\nNome do arquivo não fornecido, digite novamente!\n")
            return False
    
    elif option_save == "N":
        clean_screen()
        print("\nÉ uma pena, suas tarefas não foram salvas.\n")
        return True

    else:
        print("\nOpção inválida, digite novamente!\n")
        return False