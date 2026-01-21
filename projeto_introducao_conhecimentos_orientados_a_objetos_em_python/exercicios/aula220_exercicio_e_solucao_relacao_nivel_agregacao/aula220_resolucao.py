from aula220_1_exercicio_classes_relacoes_carro import Carro as carro
from aula220_2_exercicio_classes_relacoes_motor import Motor as motor
from aula220_3_exercicio_classes_relacoes_fabricante import Fabricante as fabricante

# Exercício com Classes
# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

criar_motor = motor.montar_motor("1.0")
criar_fabricante = fabricante.montar_fabricante("Fiat")
criar_carro = carro.montar_carro("Argo Drive", criar_motor, criar_fabricante)

criar_carro.exibir_detalhes()

criar_motor2 = motor.montar_motor("1.6")
criar_fabricante2 = fabricante.montar_fabricante("Honda")
criar_carro2 = carro.montar_carro("Civic")