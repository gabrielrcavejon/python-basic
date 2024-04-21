
def mm():
    print("Selecione a operação desejada:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def r(operacao, valor1, valor2):
    if operacao == 1:
        return valor1 + valor2
    elif operacao == 2:
        return valor1 - valor2
    elif operacao == 3:
        return valor1 * valor2
    elif operacao == 4:
        if valor2 != 0:
            return valor1 / valor2

mm()

operacao = int(input("Digite o número da operação desejada (1, 2, 3, 4): "))

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

resultado = r(operacao, valor1, valor2)

print("Resultado da operação:", resultado)