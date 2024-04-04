# 36. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

num = int(input("Digite um numero inteiro de 4 digitos: "))

print(f"Digito 1: {num // 1000}")
print(f"Digito 2: {num % 1000 // 100}")
print(f"Digito 3: {num % 100 // 10}")
print(f"Digito 4: {num % 10}")
