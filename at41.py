# 41. Faça um programa para ler as dimensões de um terreno (comprimento e largura), com
# como o preço do metro de tela. Imprima o custo para cercar este mesmo terreno com
# tela.

c = float(input("Digite o comprimento do terreno: "))
l = float(input("Digite a largura do terreno: "))
v = float(input("Digite o valor do metro de tela: "))

print(f"Custo para cercar o terreno com a tela: {(c * 2 + l * 2) * v}")
