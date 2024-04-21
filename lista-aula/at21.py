def b(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

ano = int(input("Digite o ano: "))

if b(ano):
    print("O ano", ano, "é bissexto.")
else:
    print("O ano", ano, "não é bissexto.")
  