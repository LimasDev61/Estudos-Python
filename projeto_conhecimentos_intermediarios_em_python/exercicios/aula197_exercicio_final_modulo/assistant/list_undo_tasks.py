def list_undo(tasks_undo):

    if not tasks_undo:
        print("\nNenhuma tarefa para desfazer!\n")
        return

    print("\nEssas são suas tarefas desfeitas:\n")
    for i, task in enumerate(tasks_undo, 1):
        print(f"{i} - {task}")

    print()