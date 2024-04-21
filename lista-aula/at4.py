import math

numero = float(input("Digite um número: "))

if numero > 0:
    quadrado = numero ** 2
    print("O número ao quadrado é:", quadrado)
    
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada do número é:", raiz_quadrada)
else:
    print("O número não é positivo.")
