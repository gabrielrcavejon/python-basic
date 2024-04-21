l = float(input("Digite a nota do trabalho de laboratório (entre 0 e 10): "))
s = float(input("Digite a nota da avaliação semestral (entre 0 e 10): "))
f = float(input("Digite a nota do exame final (entre 0 e 10): "))

v = (0 <= l <= 10) and (0 <= s <= 10) and (0 <= f <= 10)

if v:
    mf = (l * 2 + s * 3 + f * 5) / 10

    if mf < 3.0:
        situacao = "Reprovado"
    elif mf < 5.0:
        situacao = "Em recuperação"
    else:
        situacao = "Aprovado"

    print("Média final:", mf)
    print("Situação:", situacao)
