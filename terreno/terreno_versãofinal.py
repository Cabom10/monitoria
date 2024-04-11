def criar_terreno(tamanho): # definindo uma função chamada criar_terreno que recebe um parâmetro tamanho.
    return [[0] * tamanho for _ in range(tamanho)] #criando uma lista de tamanho elementos, cada um inicializado com zero.

def elevar(malha, x, y):
    if validar_coordenadas(malha, x, y): # as coordenadas (x, y) estão dentro dos limites da matriz malha usando a função validar_coordenadas
        malha[x][y] += 1 #Se as coordenadas forem válidas, incrementamos o valor na posição (x, y) da matriz malha em 1.
        atualizar_vizinhos(malha, x, y, 1) # atualizar os valores dos vizinhos do ponto (x, y) na matriz malha.
        imprimir_matriz(malha)

def rebaixar(malha, x, y):
    if validar_coordenadas(malha, x, y):
        malha[x][y] -= 1
        atualizar_vizinhos(malha, x, y, -1)
        imprimir_matriz(malha)

def validar_coordenadas(malha, x, y):
    tamanho = len(malha) #btemos o tamanho da matriz malha usando a função len(malha) e atribuímos a variável tamanho
    return 0 <= x < tamanho and 0 <= y < tamanho #Verificamos se as coordenadas (x, y) estão dentro dos limites da matriz malha. 
#A expressão 0 <= x < tamanho verifica se x está entre 0 e tamanho - 1, e o mesmo ocorre com y. Se ambas as condições forem verdadeiras, 
#a função retorna True, indicando que as coordenadas são válidas; caso contrário, retorna False.

def atualizar_vizinhos(malha, x, y, diferenca):
    tamanho = len(malha)
    for nx in range(x-1, x+2):   #Iteramos sobre os vizinhos da célula (x, y) na matriz malha. Para isso, usamos dois loops for aninhados, que percorrem as coordenadas
        for ny in range(y-1, y+2):   #(nx, ny) ao redor da célula (x, y). As variáveis nx e ny representam as coordenadas dos vizinhos.
            if (nx, ny) != (x, y) and validar_coordenadas(malha, nx, ny): #Verificamos se a célula (nx, ny) não é igual à célula (x, y) para evitar a atualização da própria célula. 
                malha[nx][ny] += diferenca   #Além disso, garantimos que as coordenadas (nx, ny) estejam dentro dos limites da matriz malha usando a função validar_coordenadas

def imprimir_matriz(matriz):
    #colunas
    print("  ", end="")
    for i in range(1, len(matriz)+1):
        print(f"{i:2}", end="")
    print()
    
    #linhas
    for i, linha in enumerate(matriz, start=1):
        print(f"{i:2}", end="")
        for valor in linha:
            print(f"{valor:2}", end="")
        print()

def modificar_terreno(malha):
    while True:
        entrada = input("Digite a coordenada e o sinal para alterar o terreno (x,y,+) ou digite 'pare' para encerrar as alterações: ")
        if entrada == 'pare':
            break  
        entrada = entrada.split(',')
        if len(entrada) != 3:
            print('Entrada inválida')
            continue
        try:
            x = int(entrada[0])
            y = int(entrada[1])
            sinal = 1 if entrada[2] == '+' else -1
        except ValueError:
            print('Coordenadas inválidas')
            continue
        if not validar_coordenadas(malha, x-1, y-1):
            print('Coordenadas fora dos limites do terreno')
            continue
        malha[x-1][y-1] += sinal
        atualizar_vizinhos(malha, x-1, y-1, sinal)
        imprimir_matriz(malha)

    return malha

N = 5
terreno = criar_terreno(N)

elevar(terreno, 0, 0)
elevar(terreno, 2, 2)
print("Modificação em tempo real: ")
terreno = modificar_terreno(terreno)
