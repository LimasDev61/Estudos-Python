# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# O número recebido como parâmetro

# Exemplo de closure para criar funções de fábrica
def mutiplicador(fator):
    def multiplica(numero):
        return numero * fator
    return multiplica

duplica = mutiplicador(2) 
triplica = mutiplicador(3)
quadruplica = mutiplicador(4)

print(duplica(5))      # 10
print(triplica(5))     # 15
print(quadruplica(5))  # 20