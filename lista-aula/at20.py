def ap(idade, t):
    if idade >= 65:
        return True
    elif t >= 30:
        return True
    elif idade >= 60 and t >= 25:
        return True
    else:
        return False

idade = int(input("Digite a idade: "))
t = int(input("Digite o tempo de serviço: "))

if ap(idade, t):
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador não pode se aposentar.")
