import random
def matriz(matriz):
  #colunas
  print("   ",end="")
  for i in range(1,5):
    print(f"{i:2}",end="")
  print()
  #linhas
  for i,linha in enumerate(matriz,start=1):
    for valor in linha:
      print(f"{valor:2}",end="")
  print()

def ler_valores(): #matriz 5x5
  for i in range(0,1):
    entrada=list(input().split(','))
    x=int(entrada[0])
    y=int(entrada[1])
    sinal=entrada[2]
    malha[x][y]=sinal

  return malha

malha=[[0]*5 for _ in range(5)]
ler_valores()
matriz(malha)

  