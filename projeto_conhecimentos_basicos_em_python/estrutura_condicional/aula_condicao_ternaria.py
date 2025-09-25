# Operação ternária (Condicional em uma linha)
# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso

total = 10
variavel = "maior" if total >= 9 else "menor"

print(variavel) 

# Não recomendado, pois dificulta o entendimento do código
# print("Valor" if False else "outro valor" if False else "outro outro valor")