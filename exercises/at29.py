# 29. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que
# solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que
# deverá ser paga, sabendo-se que são descontados 11% de previdência social, e após
# isso 8% para imposto de renda.

d = int(input(f"Dias trabalhados pelo encanador: "))

print(f"Pagar ao trabalhador: {30 * d - d * 0.11 - d * 0.08}")
