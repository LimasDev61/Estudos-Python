class Motor:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        if not nome or len(nome.strip()) < 1:
            print("\nO motor precisa de um nome.\n")
            return
        
        self._nome = nome

    @classmethod
    def montar_motor(cls, nome):
        return cls(nome)
