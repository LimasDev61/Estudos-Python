# Exercício - sistema de perguntas e respostas

perguntas = [
{
    "Pergunta": "Quanto é 2 + 2? ",
    "Opções": ["1", "2", "3", "4", "5"],
    "Resposta": "4",
},
{
    "Pergunta": "Quanto é 5 * 5? ",
    "Opções": ["10", "15", "20", "25", "30"],
    "Resposta": "25",
},
{
    "Pergunta": "Quanto é 10 / 2? ",
    "Opções": ["2", "3", "4", "5", "6"],
    "Resposta": "5",
}]

respostas_certas = 0
for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    
    for i, opcao in enumerate(pergunta["Opções"]):
        print(f"{i + 1}. {opcao}")

    print()
    resposta_usuario = input("Escolha uma opção (1-5): ")
    print()

    acertou = False
    escolha_int = None
    quantidade_opcoes = len(pergunta["Opções"])
    if resposta_usuario.isdigit():
        escolha_int = int(resposta_usuario) - 1

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= quantidade_opcoes:
            if pergunta["Opções"][escolha_int] == pergunta["Resposta"]:
                respostas_certas += 1
                acertou = True
    
    if acertou:
        print("Você acertou 👍!")
    else:
        print("Você errou 👎!")

    print()


print(f"Você acertou {respostas_certas} de {len(perguntas)} perguntas.")