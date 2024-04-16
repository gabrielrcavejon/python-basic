   #  - Nome
   #  - Altura (cm)
   #  - Peso (kg)
   #  Com base nestes dados realize o calculo para 
   #  descobrir qual o IMC (indice de massa corporea)
   #  da pessoa.
   #  Para o calculo utilize a tabela padrão do IMC.
   #  abaixo de 18,5 - Abaixo do Peso (Pegue suplementos do Cariani)
   #  entre 18,6 e 24,9 - Peso Ideal (Para Bens)
   #  entre 25,0 e 29,9 - Sobrepeso
   #  entre 30,0 e 34,9 - Obesidade Grau 1
   #  entre 35,0 e 39,9 - Obesidade Grau 2
   #  acima de 40,0 - Obesidade Grau 3 (Dr. Nowzaradan te espera)
   #  formula: IMC = peso / altura²

nome = input("Digite seu Nome: ")
altura = float(input("Digite sua Altura: "))
peso = float(input("Digite o segundo atual: "))

imc = peso / (altura * altura)

if (imc < 18.5):
   print(f"Abaixo do Peso")
elif(imc >= 18.6 and imc < 25):
   print(f"Peso Ideal")
elif(imc >= 25 and imc < 30):
   print(f"Sobrepeso")
elif(imc >= 30 and imc < 35):
   print(f"Obesidade Grau 1")
elif(imc >= 35 and imc < 40):
   print(f"Obesidade Grau 2")
elif(imc >= 40):
   print(f"Obesidade Grau 3")
   

