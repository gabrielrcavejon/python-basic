d = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

numero = int(input("Digite um número entre 1 e 7: "))

if 1 <= numero <= 7:
    ds = d[numero]
    print("O dia da semana correspondente a", numero, "é:", ds)
