# 30. Faça um programa que leia o valor da hora de trabalho em reais e número de horas
# trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
# o valor calculado.

v = float(input(f"Valor da hora trabalhada: "))
n = float(input(f"número de horas trabalhadas no mês: "))

print(f"Valor a pargar + 10% sobre: {v * n + (v * n * 0.1)}")
