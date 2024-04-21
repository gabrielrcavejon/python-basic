import math

numero = int(input("Digite um número: "))

if numero < 0:
    print("Número inválido.")
else:
    resultado = math.log(numero)
    print("O logaritmo do número é:", resultado)
