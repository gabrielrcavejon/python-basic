# 31. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
# sabendo-se que esse funcionário em uma gratificação de 5% sobre o salário-base.
# Além disso, ele paga 7% de imposto sobre o salário-base.

v = float(input(f"Digite o salário-base: "))

print(f"Valor a receber: {v * 1.05 - v * 0.07}")
