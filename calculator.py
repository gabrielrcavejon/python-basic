print("Escolha uma operação.")
print()
print("A - Adição")
print("S - Subtração")
print("M - Multiplicação")
print("D - Divisão")
print("X - Sair")
print()

operacao = ""

while operacao != "X" or operacao != "x":

  operacao = input()

  match operacao:
    case "A":
      n1 = int(input("Digite o primeiro numero: "))
      n2 = int(input("Digite o segundo numero: "))
      
      print(f"Resultado de {n1} + {n2} = {n1 + n2}")
      print()
    case "S":
      n1 = int(input("Digite o primeiro numero: "))
      n2 = int(input("Digite o segundo numero: "))
      
      print(f"Resultado de {n1} - {n2} = {n1 - n2}")
      print()
    case "M":
      n1 = int(input("Digite o primeiro numero: "))
      n2 = int(input("Digite o segundo numero: "))
      
      print(f"Resultado de {n1} * {n2} = {n1 * n2}")
      print()
    case "D":
      n1 = int(input("Digite o primeiro numero: "))
      n2 = int(input("Digite o segundo numero: "))
      
      print(f"Resultado de {n1} / {n2} = {n1 / n2}")
      print()
    case "X":
      break
    case _:
      print("Digite um número valido!")
      
  operacao = ""

  print("Escolha outra operação.")

  #limpar terminal

print("Obrigado por usar Calculator!")