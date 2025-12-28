from assistant import list_tasks, list_undo, clean_screen


def redo_tasks(undo_task, tasks_add):

    if not undo_task:
        clean_screen()
        print("\nNenhuma tarefa para refazer!\n")
        return False
    
    clean_screen()
    task = undo_task.pop()
    tasks_add.append(task)

    if len(undo_task) > 0:
        list_undo(undo_task)

    print(f"-> A tarefa '{task}' foi refeita.\n")

    list_tasks(tasks_add)