import math

numero = float(input("Digite um número: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é:", raiz_quadrada)
else:
    print("Número inválido. O número deve ser positivo.")