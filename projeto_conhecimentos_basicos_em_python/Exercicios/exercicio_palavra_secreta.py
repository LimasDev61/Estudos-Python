"""

Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, você vai conferir se a
letra digitada está na palavra secreta.
....- Se a letra digitada estiver na palavra secreta, exiba a letra.
....- Se a letra digitada não estiver na palavra secreta, exiba *.
Faça a contagem de tentativa do seu usuário.

"""
import os

palavra_secreta = "Brasil".lower()
letras_descobertas = ""
tentativas = 0

print(f"\nJogo da palavra secreta, a palavra escolhida tem {len(palavra_secreta)} letras")

while True:
    digite_uma_letra = input("\nTente adivinhar, digite apenas uma letra: ")

    tentativas += 1

    if len(digite_uma_letra) > 1:
        print("\nDigite apenas uma letra")
        continue
        
    if digite_uma_letra in palavra_secreta:
        letras_descobertas += digite_uma_letra

    if digite_uma_letra in palavra_secreta:
        print("\nAcertou uma Letra!")
    else:
        print("\nErrou")
    
    acertos = 0
    palavra_formada = ""
    for letra in palavra_secreta:
        if letra in letras_descobertas:
            palavra_formada += letra
            acertos += 1
        else:
            palavra_formada += "*"
    

    print(f"\nVocê acertou {acertos} de {len(palavra_secreta)} letras: {palavra_formada}")

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print(f"\nParabéns você acertou a palavra {palavra_secreta} em {tentativas} tentativas!")
        break

