# Lendo os dados da primeira peça
codigo1, quantidade1, valor_unitario1 = map(float, input().split())


codigo2, quantidade2, valor_unitario2 = map(float, input().split())


total = quantidade1 * valor_unitario1 + quantidade2 * valor_unitario2


print("VALOR A PAGAR: R$ {:.2f}".format(total))