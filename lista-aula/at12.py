nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

m = (nota1 * 1 + nota2 * 2) / 3

if m >= 70:
    print("Média do aluno:", m)
    print("Aluno aprovado")
else:
    print("Média do aluno:", m)
    print("Aluno reprovado")
