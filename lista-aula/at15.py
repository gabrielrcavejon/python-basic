# Função para imprimir o mês correspondente ao número usando match-case
def i(numero):
    match numero:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Março")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")
        case _:
            print("Número inválido. Digite um número entre 1 e 12.")

numero = int(input("Digite um número entre 1 e 12: "))

i(numero)
