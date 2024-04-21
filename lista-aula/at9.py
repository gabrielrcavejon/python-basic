s = float(input("Digite o salário do trabalhador: "))
p = float(input("Digite o valor da prestação do empréstimo: "))

l = 0.2 * s

if p > l:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
  
