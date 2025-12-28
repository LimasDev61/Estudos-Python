# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
# Recursão, aprendizado:
# https://panda.ime.usp.br/pensepy/static/pensepy/12-Recursao/recursionsimple-ptbr.html

# Recursão - padrão LiFO (Last In, First Out)
#
# Cada chamada da função armazenada na estrutura de callstack, é chamada de "frame" 
# ou "call frame".
# Cada frame contém informações sobre a chamada da função, como os parâmetros
# passados, variáveis locais e o ponto de retorno.
#
# A pilha de chamadas (call stack) funciona como uma pilha de pratos(pratos, são frames): 
# o último prato a ser colocado na pilha é o primeiro a ser retirado. Assim, quando uma 
# função é chamada, ela é adicionada ao topo da pilha, e quando a função termina sua 
# execução, ela é removida do topo da pilha.
#
# Exemplo:
# IDA >
# Criando a pilha de chamadas(Call Stack) - nome da função e o estado dos parâmetros:
# PRATO 1 (base da pilha) - main() - chamada inicial
# PRATO 2 - segunda chamada da função atual
# PRATO 3 - segunda chamada da função atual
# PRATO 4 - (topo da pilha) ultima chamda da função atual
#
# Caso base - condição de parada
#
# VOLTA <
# Descarregando a pilha de chamadas(Call Stack) - nome da função
# PRATO 4 - (topo da pilha) ultima chamada da função atual
# PRATO 3 - segunda chamada da função atual
# PRATO 2 - segunda chamada da função atual
# PRATO 1 (base da pilha) - main() - chamada inicial

print("\nCarregando a Pilha de Chamadas(Call Stack) - Contagem na IDA da recursão:")
def contar(inicio, fim):
    print("Call Frame(First in): ", inicio) # Contagem na IDA da recursão carregamento da pilha
    
    # Caso base - condição de parada
    if inicio == fim:
        print("\nDescarregando a Pilha de Chamadas(Call Stack) - Contagem na VOLTA da recursão:")
        print("Call Frame(Last out): ", inicio) # Imprime o último numero da contagem
        return
    
    # Caso recursivo(Motor) - chamada da função com um problema menor
    contar(inicio + 1, fim)

    # Chamada só acontece, após o caso base ser alcançado, a função morre e acontece o
    # descarregamento da pilha de chamadas(Call Stack)
    print("Call Frame(Last out): ", inicio) # Contagem na VOLTA da recursão - descarregamento da pilha

contar(1, 4)

# Exemplo de Stack Overflow - estouro da pilha de chamadas(Call Stack)
# Acontece quando não utilizamos a regra de ouro das funções recursivas:
# - Um caso base que para a recursão (Condição de parada)
# - Ou desconhecer o limite máximo de recursão da linguagem
# Em Python, o limite padrão de recursão é 1000 chamadas. Podemos verificar e alterar
# com o modulo sys.

