# 40. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
# proporcionalmente ao valor que cada um deu para a realização da aposta. Faça um
# programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
# quanto cada um ganharia do prêmio com base no valor investido

j1 = float(input("Digite o valor que o jogador 1 apostou: "))
j2 = float(input("Digite o valor que o jogador 2 apostou: "))
j3 = float(input("Digite o valor que o jogador 3 apostou: "))
v = float(input("Digite o valor do premio: "))

t = j1 + j2 + j3

print(f"Jogador 1 ganhou: {100 * j1 / t * t}")
print(f"Jogador 2 ganhou: {100 * j2 / t * t}")
print(f"Jogador 3 ganhou: {100 * j3 / t * t}")
