# 38. Faça um programa que leia o horário (hora, minuto e segundo) do início e a duração
# em segundo

h = int(input("Digite a hora atual: "))
m = int(input("Digite o minuto atual: "))
s = int(input("Digite o segundo atual: "))

d = int(input("Digite a duracao em segundos: "))

totalSegundos = h * 3600 + m * 60 + s + d

print(f"Horario {10 % 60} termino: {totalSegundos // 3600}:{(totalSegundos % 3600) // 60}:{(totalSegundos % 3600) % 60}")
