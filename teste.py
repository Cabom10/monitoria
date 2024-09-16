# Definindo a estrutura de registro
class Registro:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

# Criando a matriz de registros
matriz = [
    [Registro(2, 1), Registro(4, 3)],
    [Registro(6, 2), Registro(1, 5)],
    [Registro(3, 4), Registro(5, 6)]
]

# Inicializando o vetor e a soma
vetor = [0, 0]
soma = 0

# Preenchendo o vetor com base na matriz
for i in range(3):
    for j in range(2):
        vetor[j] += matriz[i][j].valor * matriz[j][j % 2].peso

# Calculando a soma condicional
for k in range(2):
    if vetor[k] > 15:
        soma += vetor[k] * (k + 2)

# Exibindo o resultado
print(soma)
