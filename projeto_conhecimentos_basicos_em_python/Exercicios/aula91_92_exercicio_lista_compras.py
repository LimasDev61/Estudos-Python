# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de 
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com erros de indexes inexistente
import os

compras = []

while True:
    print("\nEscolha uma opção:")
    print("1 - Inserir um item na lista")
    print("2 - Remover um item da lista")
    print("3 - Listar os itens da lista")
    print("4 - Sair do programa")

    opcao = input("\nDigite a opção desejada: ")
    
    try:
        opcao_int = int(opcao)
    except ValueError:
        print("Opção inválida. Por favor, digite um número inteiro.")
        continue

    if opcao_int == 1:
        os.system("clear")
        while True:
            adicionar = input("Digite um item para ser adicionado à lista (ou 'sair' para encerrar): ").lower()

            if not adicionar:
                print("Por favor, digite um item para adicionar.")
    
            if adicionar == "sair":
                print()
                break
            
            elif adicionar not in compras and adicionar:
                compras.append(adicionar)
                print(f"Item '{adicionar}' adicionado com sucesso, agora sua lista possui", len(compras), "itens!")
            else:
                print("O item já existe na lista.")
    
    elif opcao_int == 2:
        os.system("clear")
        while True:
            remover = input("Digite um item para ser removido da lista (ou 'sair' para encerrar): ").lower()

            if remover == "sair":
                print()
                break

            try:
                indice = int(remover) - 1
                item_removido = compras[indice]
                del compras[indice]
                print(f"Item '{item_removido}' removido com sucesso, agora sua lista possui", len(compras), "itens!")
            except ValueError:
                print("Opção inválida. Por favor, digite um número inteiro.")
            except IndexError:
                print("O indice informado não existe na lista.")

    elif opcao_int == 3:
        os.system("clear")
        print("Itens na sua lista:")
        if not compras:
            print("Sua lista de compras está vazia.\n")
        else:
            for index, item in enumerate(compras, start=1):
                print(f"{index} - {item}")

    elif opcao_int == 4:
        os.system("clear")
        print("Encerrando o programa...")
        break