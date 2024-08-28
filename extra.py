# Definindo a estrutura TConjunto usando uma classe em Python
class TConjunto:
    def __init__(self):
        # Inicializa um conjunto vazio com capacidade máxima de 20 elementos
        self.elementos = []
        self.n = 0

# a) Função para criar um conjunto vazio
def criar_conjunto():
    return TConjunto()

# b) Função para ler os dados de um conjunto
def ler_conjunto(conjunto, elementos):
    for elemento in elementos:
        if len(conjunto.elementos) < 20:  # Verifica se há espaço no conjunto
            conjunto.elementos.append(elemento)
            conjunto.n += 1
        else:
            print("O conjunto já atingiu o tamanho máximo de 20 elementos.")
            break

# c) Função para fazer a união de dois conjuntos
def uniao_conjuntos(conjunto1, conjunto2):
    conjunto_uniao = criar_conjunto()
    conjunto_uniao.elementos = conjunto1.elementos.copy()
    
    for elemento in conjunto2.elementos:
        if elemento not in conjunto_uniao.elementos and len(conjunto_uniao.elementos) < 20:
            conjunto_uniao.elementos.append(elemento)
    
    conjunto_uniao.n = len(conjunto_uniao.elementos)
    return conjunto_uniao

# d) Função para fazer a interseção de dois conjuntos
def intersecao_conjuntos(conjunto1, conjunto2):
    conjunto_intersecao = criar_conjunto()
    
    for elemento in conjunto1.elementos:
        if elemento in conjunto2.elementos:
            conjunto_intersecao.elementos.append(elemento)
    
    conjunto_intersecao.n = len(conjunto_intersecao.elementos)
    return conjunto_intersecao

# e) Função para verificar se dois conjuntos são iguais
def conjuntos_iguais(conjunto1, conjunto2):
    if conjunto1.n != conjunto2.n:
        return False
    
    for elemento in conjunto1.elementos:
        if elemento not in conjunto2.elementos:
            return False
    
    return True

# f) Função para imprimir um conjunto
def imprimir_conjunto(conjunto):
    print("Conjunto:", conjunto.elementos)

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
