'''
Me chamo Gabriel Rodrigo Cavejon, este arquivo calculator.py, na data 16/05/2024 fiz esse projeto
'''

print("Escolha uma operação.")
print()
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("X - Sair")
print()

operacao = ""

while operacao != "X" or operacao != "x":

  operacao = input()
  resultado = 0

  '''
    MATCH CASE principal, dentro de um while, ate quando nao for igual a X ou x que é sair
  '''

  match operacao: # AQUI vai ser escolhido o que vai ser feito com base no que o usuario digitou
    case "1": 
      while True:
        num = input("Digite um numero ou aperte P para calcular: ")

        if num == "P":
          print(f"Resultado é {resultado}")
          break

        resultado = resultado + float(num)
      print()
    case "2":
      while True:
        num = input("Digite um numero ou aperte P para calcular: ")

        if num == "P":
          print(f"Resultado é {resultado}")
          break
        
        if resultado == 0:
          resultado = float(num)
          print(resultado)
        else:
          resultado = resultado - float(num)
          print(resultado)

      print()
    case "3":
      while True:
        num = input("Digite um numero ou aperte P para calcular: ")

        if num == "P":
          print(f"Resultado é {resultado}")
          break
        
        if resultado == 0:
          resultado = float(num)
        else:
          resultado = resultado * float(num)

      print()
    case "4":
      while True:
        num = input("Digite um numero ou aperte P para calcular: ")

        if num == "P":
          print(f"Resultado é {resultado}")
          break
        
        if resultado == 0:
          resultado = float(num)
        else:
          resultado = resultado / float(num)

      print()
    case "X":
      break
    case _: # AQUI quando foi algo que nao é 1, 2, 3, 4 ou X
      print("Digite um número valido!")
      
  operacao = ""
  resultado = 0

  print("Escolha outra operação.")


print("Obrigado por usar Calculator!")