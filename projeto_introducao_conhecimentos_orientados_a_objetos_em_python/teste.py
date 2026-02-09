class A:
    def fala(self):
        print("Fala de A")

class B(A):
    def fala(self):
        print("Fala de B")

class C(A):
    def fala(self):
        print("Fala de C")

# Resultado da ordem de resolução de métodos (MRO) para a classe D
class D(B, C):
    pass

# Qual será a saída?
objeto = D()
objeto.fala() # Saída: "Fala de B" 

print(D.mro())
# Ordem: D -> B -> C -> A -> object