# 32. Escreva um programa de ajuda para vendedor. A partir de um valor total lido mostre:
# a. O total a pagar com desconto de 10%;
# b. O valor de cada parcela, no parcelamento de 3x sem juros;
# c. A comissão do vendedor, caso de a venda ser a vista (5% sobre o valor com
# desconto);
# d. A comissão do vendedor, caso de a venda ser parcelada (5% sobre o valor
# total)

v = float(input(f"Digite o o valor total: "))

print(f"Total a pagar com desconto de 10%: {v - v * 0.1}")
print(f"Valor de cada parcela, no parcelamento de 3x sem juros:")
print(f"    - Parcela 1: {v/3}")
print(f"    - Parcela 2: {v/3}")
print(f"    - Parcela 3: {v/3}")
print(f"Comissão do vendedor, caso de a venda ser a vista (5% sobre o valor com desconto): {v * 0.9 * 0.05}")
print(f"comissão do vendedor, caso de a venda ser parcelada (5% sobre o valor total): {v * 0.05}")
