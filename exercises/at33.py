# 33. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
# subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para
# atingir seu objetivo.

d = float(input(f"Altura do degrau da escada: "))
a = float(input(f"Altura que deseja alcançar: "))

print(f"Qtd de degraus para subir: {a / d}")
