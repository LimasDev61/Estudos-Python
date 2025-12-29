# Constante = "Variáveis" que não mudam de valor
# Constantes são escritas em MAIÚSCULO_COM_SOBRELINHADOS
# Complexidade de código = Quanto mais complexo, mais difícil de entender e manter
# Código complexo = Mais propenso a erros
# Código simples = Menos propenso a erros
# Muitas condições no mesmo if, while, for = Código complexo
# ... <- Contagem de complexidade - sempre que possível manter a complexidade baixa

velocidade_carro = 80  # velocidade atual do carro
local_carro = 99      # local em que o carro está na estrada

RADAR_1 = 60          # velocidade máxima do radar 1
LOCAL_RADAR_1 = 100   # local onde o radar 1 está na estrada
RADAR_RANGE = 1       # Distância em quilometros que o radar pega

antes_ranger = LOCAL_RADAR_1 - RADAR_RANGE
depois_ranger = LOCAL_RADAR_1 + RADAR_RANGE

velocidade_carro_passou_radar = velocidade_carro > RADAR_1
carro_passou_radar1 = antes_ranger <= local_carro <= depois_ranger # 99 <= 100 <= 101

if velocidade_carro_passou_radar and carro_passou_radar1:
    print("MULTADO NO RADAR 1")
else:
    print("Não foi multado no radar 1")

if carro_passou_radar1:
    print("Carro passou no radar 1")
