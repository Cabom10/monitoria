# Definindo a estrutura TConjunto usando uma classe em Python
class TConjunto:
    def __init__(self):
        # Inicializa um conjunto vazio com capacidade máxima de 20 elementos
        self.elementos = [0] * 20  # Array fixo de 20 posições
        self.n = 0  # Tamanho atual do conjunto

# Função para criar um conjunto vazio
def criar_conjunto():
    return TConjunto()

# Função para ler os dados de um conjunto
def ler_conjunto(conjunto, elementos):
    for elemento in elementos:
        if conjunto.n < 20:  # Verifica se há espaço no conjunto
            conjunto.elementos[conjunto.n] = elemento
            conjunto.n += 1
        else:
            print("O conjunto já atingiu o tamanho máximo de 20 elementos.")
            break

# Função para verificar se um elemento está no conjunto
def elemento_presente(conjunto, elemento):
    for i in range(conjunto.n):
        if conjunto.elementos[i] == elemento:
            return True
    return False

# Função para fazer a união de dois conjuntos
def uniao_conjuntos(conjunto1, conjunto2):
    conjunto_uniao = criar_conjunto()

    # Adiciona todos os elementos do conjunto1
    for i in range(conjunto1.n):
        conjunto_uniao.elementos[conjunto_uniao.n] = conjunto1.elementos[i]
        conjunto_uniao.n += 1

    # Adiciona os elementos de conjunto2 que não estão em conjunto1
    for i in range(conjunto2.n):
        if not elemento_presente(conjunto_uniao, conjunto2.elementos[i]) and conjunto_uniao.n < 20:
            conjunto_uniao.elementos[conjunto_uniao.n] = conjunto2.elementos[i]
            conjunto_uniao.n += 1
    
    return conjunto_uniao

# Função para fazer a interseção de dois conjuntos
def intersecao_conjuntos(conjunto1, conjunto2):
    conjunto_intersecao = criar_conjunto()

    for i in range(conjunto1.n):
        if elemento_presente(conjunto2, conjunto1.elementos[i]):
            conjunto_intersecao.elementos[conjunto_intersecao.n] = conjunto1.elementos[i]
            conjunto_intersecao.n += 1

    return conjunto_intersecao

# Função para verificar se dois conjuntos são iguais
def conjuntos_iguais(conjunto1, conjunto2):
    if conjunto1.n != conjunto2.n:
        return False
    
    for i in range(conjunto1.n):
        if not elemento_presente(conjunto2, conjunto1.elementos[i]):
            return False
    
    return True

# Função para imprimir um conjunto
def imprimir_conjunto(conjunto):
    print("Conjunto: ", end="")
    for i in range(conjunto.n):
        print(conjunto.elementos[i], end=" ")
    print()

# Exemplos de uso:
# Criando dois conjuntos
conjunto1 = criar_conjunto()
conjunto2 = criar_conjunto()

# Adicionando elementos aos conjuntos
ler_conjunto(conjunto1, [1, 2, 3, 4, 5])
ler_conjunto(conjunto2, [4, 5, 6, 7, 8])

# Imprimindo os conjuntos
imprimir_conjunto(conjunto1)
imprimir_conjunto(conjunto2)

# União dos conjuntos
conjunto_uniao = uniao_conjuntos(conjunto1, conjunto2)
imprimir_conjunto(conjunto_uniao)

# Interseção dos conjuntos
conjunto_intersecao = intersecao_conjuntos(conjunto1, conjunto2)
imprimir_conjunto(conjunto_intersecao)

# Verificando se os conjuntos são iguais
print("Conjuntos são iguais:", conjuntos_iguais(conjunto1, conjunto2))
