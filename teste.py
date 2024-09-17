def contar_digitos(P):
    total_digitos=0
    atual=1
    while atual <=P:
        proximo=atual*10
        limiteSup=min(P,proximo-1)

        total_folhas=limiteSup-atual+1

        total_digitos+= total_folhas * len(str(atual)) 

        atual=proximo  
    return total_digitos




P=int(input("Digite a quantidade de paginas: "))   

print("Total digitos: ",contar_digitos(P))

