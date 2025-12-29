# Calculadora com while

while True:
    resposta = input("Quer entrar na calculadora? [s]im / [n]ão: ").lower()

    if resposta.startswith("n"):
        print("Saindo...")
        break

    elif resposta.startswith("s"):
        try:
            digito1 = input("Digite o primeiro número: ")
            digito2 = input("Digite o segundo número: ")

            num1 = float(digito1)
            num2 = float(digito2)

            operacao = input("Digite a operação (+, -, *, /, %): ")
            
            if operacao == "+":
                print(f"{num1} + {num2} = {num1 + num2}")
                
            elif operacao == "-":
                print(f"{num1} - {num2} = {num1 - num2}")
            
            elif operacao == "*":
                print(f"{num1} * {num2} = {num1 * num2}")
            
            elif operacao == "/":
                if num2 == 0:
                    print("Não é possível dividir por zero!")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
            
            elif operacao == "%":
                percentual = num1 / 100.0
                resultado = num2 * percentual
                print(f"{num1}% de {num2} = {resultado:.2f}%")
            
            else:
                print("Operação inválida!")
                print("As operações válidas são: +, -, *, /, %\n")
                continue

        except ValueError:
            print("Entrada inválida! Por favor, insira números válidos.")
            continue

    print("\nCalculo Encerrado.\n")