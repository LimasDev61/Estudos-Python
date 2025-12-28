import json as js

def save_data(tasks_data, nome_caminho_arquivo):

    path_archive = r"C:/Users/USUARIO1/Documents/Python - Learning/Estudos-Python/projeto_conhecimentos_intermediarios_em_python/exercicios/aula197_exercicio_final_modulo/tasks_for_you"
    path_name = f"{path_archive}/{nome_caminho_arquivo}.json"

    numarate_tasks = [
        {"id": i, "tarefa": task}
        for i, task in enumerate(tasks_data, 1)
    ]
    dados_para_salvar = {
        "nome_do_arquivo": nome_caminho_arquivo,
        "quantidade_de_tarefas": len(tasks_data),
        "tarefas": numarate_tasks
    }
    
    try:
        with open(path_name, "x", encoding="utf-8") as archive:
            
            js.dump(dados_para_salvar, archive, ensure_ascii=False, indent=4)

        print(f"\nArquivo salvo com sucesso, nome: {nome_caminho_arquivo}\n")
        return True
    
    except FileExistsError:
        print(f"\nArquivo com o nome {nome_caminho_arquivo} já existe!\n")
        return False