class Carro:
    def __init__(self, nome, motor=None, fabricante=None):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

    @property
    def motor(self):
        return self._motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    @classmethod
    def montar_carro(cls, nome, motor=None, fabricante=None):
        if motor is None or fabricante is None:
            print("Motor: N/A")
            print("Fabricante: N/A")
            print(f"Carro: {nome}\n")
        
        return cls(nome, motor, fabricante)
    
    def exibir_detalhes(self):
        if self.motor:
            print(f"Motor: {self.motor.nome}")
        if self.fabricante:    
            print(f"Fabricante: {self.fabricante.nome}")
        
        print(f"Carro: {self.nome}\n")

        return True