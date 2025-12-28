from assistant import list_tasks, list_undo, clean_screen

def undo_tasks(tasks_add, undo_task):
    

    if not tasks_add:
        clean_screen()
        print("\nNenhuma tarefa para desfazer!\n")
        return False
    
    clean_screen()
    task = tasks_add.pop()
    undo_task.append(task)

    if len(tasks_add) > 0:
        list_tasks(tasks_add)

    print(f"-> A tarefa '{task}' foi desfeita.\n")
    list_undo(undo_task)


