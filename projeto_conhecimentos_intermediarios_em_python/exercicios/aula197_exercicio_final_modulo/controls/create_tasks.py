from assistant import list_tasks
from assistant import clean_screen

def create_task(tasks_add, tasks_names):
    clean_screen()
    modified_task = tasks_names.strip().capitalize()
    
    if not modified_task:
        print("\nTarefa vazia, digite novamente!\n")
        return False
    
    if modified_task in tasks_add:
        print(f"\nErro: A tarefa '{modified_task}' já existe na sua lista!\n")
        return False
    

    tasks_add.append(modified_task)

    list_tasks(tasks_add)
    
    print(f"-> A tarefa '{modified_task}' foi adicionada com sucesso.\n")
    print("\n--> Para voltar ao menu principal, digite '4' <--\n")