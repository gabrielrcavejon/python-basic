def validar_nota(nota):
    return 0.0 <= nota <= 10.0

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if validar_nota(nota1) and validar_nota(nota2):
    media = (nota1 + nota2) / 2
    print("A média das notas é:", media)
