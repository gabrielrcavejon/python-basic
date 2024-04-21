import math

numero = float(input("Digite um número: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz de", numero, "é:", raiz_quadrada)
else:
    numero_quadrado = numero ** 2
    print("O número", numero, "ao quadrado é:", numero_quadrado)