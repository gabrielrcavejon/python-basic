# 45. Calcule a média de um aluno na disciplina de ED. Para isso solicite o nome do aluno, a
# nota da prova e a nota qualitativa. Sabe-se que a nota da prova tem peso 2 e a nota
# qualitativa peso 1. Mostre a média como resultado.

nome = input("Nome do aluno: ")
n1 = float(input("Nota da prova: "))
n2 = float(input("Nota qualificativa: "))

media = (n1 * 2 + n2) / 3

print(f"Media de {nome}: {media}")
