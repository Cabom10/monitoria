def criar_terreno(tamanho):
    return [[0] * tamanho for _ in range(tamanho)]

def elevar(malha, x, y):
    if validar_coordenadas(malha, x, y):
        malha[x][y] += 1
        atualizar_vizinhos(malha, x, y, 1)
        imprimir_matriz(malha)

def rebaixar(malha, x, y):
    if validar_coordenadas(malha, x, y):
        malha[x][y] -= 1
        atualizar_vizinhos(malha, x, y, -1)
        imprimir_matriz(malha)

def validar_coordenadas(malha, x, y):
    tamanho = len(malha)
    return 0 <= x < tamanho and 0 <= y < tamanho

def atualizar_vizinhos(malha, x, y, diferenca):
    tamanho = len(malha)
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            if (nx, ny) != (x, y) and validar_coordenadas(malha, nx, ny):
                malha[nx][ny] += diferenca

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
