# 24. Sejam 𝑏 e 𝑏 os catetos de um triangulo.Faça um programa que receba 
# os valores de 𝑎 e 𝑏 e calculo o valor da hipotenusa através da equação. 
# Imprima o resultado dessa operação.

a = float(input(f"Digite o cateto a: "))
b = float(input(f"Digite o cateto b: "))

print(f"Valor da hipotenusa: {(a * a + b * b)**(1/2)}")
