# Importando diretamente dos arquivos na mesma pasta
from controls.create_tasks import create_task
from controls.undo_tasks import undo_tasks
from controls.redo_tasks import redo_tasks
from controls.exit_handler import handle_exit

def start_options(options, tasks, tasks_undo, task_names = None):

    if not options:
        print("\nOpção inválida, digite novamente!\n")
        return False
    
    if options not in ["1", "2", "3", "4"]:
        print("\nOpção inválida, digite novamente, números de 1 a 4\n")
        return False

    dict_task = {
        "1": lambda: create_task(tasks, task_names),
        "2": lambda: undo_tasks(tasks, tasks_undo),
        "3": lambda: redo_tasks(tasks_undo, tasks),
        "4": lambda: handle_exit(tasks)
    }

    final = dict_task.get(options, lambda: None)
    return final()