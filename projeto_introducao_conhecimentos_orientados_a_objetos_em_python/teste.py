class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

class Caneta:
    def escrever(self):
        print("A caneta está escrevendo...")

escritor = Escritor("Renan")
caneta_azul = Caneta()

# Associação: o escritor passa a usar a caneta
escritor.ferramenta = caneta_azul
escritor.ferramenta.escrever() # A caneta está escrevendo...