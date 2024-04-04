# 43. O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a
# quantidade de cada item que você consumiu e calcule a conta final.
# a. Hambúrguer........ R$ 3,00
# b. Cheeseburger...... R$ 2,50
# c. Fritas............ R$ 2,50
# d. Refrigerante ..... R$ 1,00
# e. Milkshake......... R$ 3,00

a = int(input("Digite a qtd que consumiu de Hambúrguer: "))
b = int(input("Digite a qtd que consumiu de Cheeseburger: "))
c = int(input("Digite a qtd que consumiu de Fritas: "))
d = int(input("Digite a qtd que consumiu de Refrigerante: "))
e = int(input("Digite a qtd que consumiu de Milkshake: "))

print(f"Valor a pagar: {a * 3 + b * 2.50 + c * 2.50 + d * 1 + e * 3}")
