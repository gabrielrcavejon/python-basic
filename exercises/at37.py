# 37. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

s = int(input("Digite um valor inteiro em segundos: "))

print(f"Horas: {s // 3600}")
print(f"Munutos: {s % 3600 // 60}")
print(f"segundos: {(s % 3600) % 60}")
