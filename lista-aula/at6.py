n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    a = n1
else:
    a = n2

d = abs(n1 - n2)

print("O maior número é:", a)
print("A diferença entre os números é:", d)
