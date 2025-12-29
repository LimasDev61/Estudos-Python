# Aula 37 -> Debugger no VS Code e Interpretador Python
#
# Para depurar, é preciso criar um breakpoint(ponto de interrupção) na parte próximo aos números das linhas
# do código(ou apertar F9 para criar ou deletar o breakpoint na linha).
#
# O Breakpoint, é um ponto de parada  que indica onde o programa deve pausar sua execução.
# Isso permite que você examine o estado das variáveis e a ordem de execução do código.
#
# Para deupurar no VS Code, é necessário ir na seção de depuração(sinal de play com um besouro). A primeira
# vez que você for depurar, o VS code vai pedir para que crie um arquivo launch.json, ele pode ser
# configurado no padrão ou personalizado.

# 1. Para começar a depurar, faça o seguinte:
#
# 1. Coloque breakpoints nas linhas desejadas(F9 ou Clique com o botão esquerdo na linha numerada).
# 2. Vá na seção de depuração no VS Code.
# 3. Clique no botão verde de play "Iniciar Depuração" ou aperte F5.
# 4. O programa vai iniciar e pausar na primeira linha com breakpoint.
# 5. Use os botões de controle na parte superior para avançar linha por linha (Step Over - F10) passa por cima das linhas,
#    entrar em funções (Step Into - F11), sair de funções (Step Out - Shift+F11) ou 
#    continuar a execução até o próximo breakpoint (Continue - F5).
#
# -> Entrar (F11): Entrar na função chamada.
# -> Sair(Shift+F11): Sai da função atual e retorna para a linha onde a função foi chamada.
# -> Avançar (F10): Avançar uma linha.
# -> Reiniciar (Ctrl+Shift+F5): Reinicia a sessão de depuração do início.
#

# 2. Painéis úteis durante a depuração
#
# -> Painel de Variáveis: Exibe todas as variáveis do escopo atual e seus respectivos valores.
#    Conforme você avança linha por linha, podemos ver os valores das variáveis mudando.
#
# -> Painel de Pontos de Interrupção: Lista todos os breakpoints definidos no código, podendo ativá-los ou desativá-los.
#
# -> Painel Console de Depuração: Um terminal interativo onde você pode executar comandos Python em tempo real.
#    enquanto o programa está pausado. Podendo por exemplo, inspecionar variáveis ou executar funções - apenas digitando
#    o nome da variável ou função e apertando enter.
#
# -> Painel Pilha de Chamadas: Mostra a sequência de chamadas de funções que levaram ao ponto atual de execução.
#    Isso é útil para entender o fluxo do programa e como chegou a determinado ponto.
#
# -> Painel de Watch: Permite adicionar expressões específicas para monitorar seus valores conforme o programa é executado.
# Exemplo: adicionar uma variável ou expressão matemática para ver como seu valor muda.

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')