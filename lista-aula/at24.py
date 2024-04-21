def calcular(c, partida):
    hc, mc = c
    hp, mp = partida

    mc = hc * 60 + mc
    mp = hp * 60 + mp
    t = mp - mc

    th = -(-t // 60)

    if th <= 2:
        preco = th * 1
    elif th <= 4:
        preco = 2 * 1 + (th - 2) * 1.4
    else:
        preco = 2 * 1 + 2 * 1.4 + (th - 4) * 2

    return preco

ch = int(input("Hora de chegada: "))
cm = int(input("Minuto de chegada: "))
chegada = (ch, cm)

ph = int(input("Hora de partida: "))
pm = int(input("Minuto de partida: "))
partida = (ph, pm)

preco = calcular(chegada, partida)
print("O preço cobrado pelo estacionamento é R$", preco)
