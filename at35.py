# 35. Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
# Gere outro numero formado pelos dígitos invertidos do número lido

num = int(input("Digite um numero inteiro de 3 digitos: "))

d1 = num // 100
d2 = (num % 100) // 10
d3 = num % 10

n = d3 * 100 + d2 * 10 + d1

print(f"O numero invertido e: {n}")
