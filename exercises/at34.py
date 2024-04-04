# 34. Faça um programa para converter uma letra maiúscula em letra minúscula. Use a
# tabela ASCII para resolver o problema.

l = input("Digite uma letra maiuscula: ")

print(f"Letra minuscula: {chr(ord(l) + 32)}")
