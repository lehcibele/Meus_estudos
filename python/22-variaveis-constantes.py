"""
CONSTANTE = "variaveis" que não vão mudar (Em python não tem essa variavel constante)
CONSTANTE = é usado com letra maisculas para identificar as constantes
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 # Velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1 # Verifica se a velocidade do carro passou do radar 1

carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')
    
if carro_multado_radar_1 and velocidade_carro_passou_radar_1:
    print('Carro multado em radar 1')