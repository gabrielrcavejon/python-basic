def c(valor, estado):
    t = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

    if estado in t:
        v = valor * (1 + t[estado])
        return v
    else:
        return None

valor = float(input("Digite o valor do produto: "))
estado = input("Digite o estado destino do produto (MG, SP, RJ, MS): ")

p = c(valor, estado)
if p is not None:
    print("O preço para o estado", estado, "é R$", p)
else:
    print("Erro: Estado inválido.")
