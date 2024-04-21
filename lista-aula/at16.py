def c(bm, be, a):
    if bm <= 0 or be <= 0:
        print("As bases devem ser maiores que zero.")
        return None
    area = ((bm + be) * a) / 2
    return area

bm = float(input("Digite o valor da base maior do trapézio: "))
be = float(input("Digite o valor da base menor do trapézio: "))
a = float(input("Digite o valor da altura do trapézio: "))

area_trapezio = c(bm, be, a)

if area_trapezio is not None:
    print("A área do trapézio é:", area_trapezio)
