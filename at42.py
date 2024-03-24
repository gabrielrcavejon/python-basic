# 42. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
# porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica.
# Supondo que a porcentagem do distribuidor seja de 12% e a dos impostos de 45%,
# prepare um algoritmo para ler o custo de fábrica do carro e imprimir o custo ao
# consumidor.

c = float(input("Digite o custo de fabrica do carro: "))

print(f"Custo para consumidor final: {c + c * 0.12 + c * 0.45}")
