from .clear_console import clean_screen

def list_tasks(tasks):

    if not tasks:
        clean_screen()
        print("\nNenhuma tarefa cadastrada!\n")
        return False
    
    print("\nEssas são suas tarefas:\n")
    for i, task in enumerate(tasks, 1):
        print(f"{i} - {task}")

    print(f"\nVocê tem {len(tasks)} tarefa(s) cadastrada(s).")