ano = int(input("Digite o ano desejado: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0): #verifica se o ano, que foi fornecido é bissexto
  explicacao = f"O ano {ano} é bissexto, ele possui 366 dias."
else:
  explicacao = f"O ano {ano} não é bissexto, ele possui 365 dias."

print(explicacao)
