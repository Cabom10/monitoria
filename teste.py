import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configurações iniciais
distancia_ate_praia = 3  # Distância do farol até a praia (km)
velocidade_angular = 16 * np.pi  # Velocidade angular (radianos por minuto)

# Função de inicialização da animação
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point, annotation

# Função de animação
def animate(t):
    # Calcula o ângulo em radianos
    angulo = velocidade_angular * t / 60
    # Calcula a posição ao longo da praia
    x_ponto_contato = distancia_ate_praia * np.tan(angulo)
    y_ponto_contato = 0

    # Atualiza a linha do raio de luz
    line.set_data([0, x_ponto_contato], [0, y_ponto_contato])
    # Atualiza o ponto de contato
    point.set_data(x_ponto_contato, y_ponto_contato)
    
    # Atualiza a anotação
    annotation.set_text(f'Ângulo: {np.degrees(angulo):.1f}°\nPonto: ({x_ponto_contato:.2f}, {y_ponto_contato:.2f})')
    annotation.set_position((x_ponto_contato, y_ponto_contato))
    
    return line, point, annotation

# Configura o gráfico
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)
line, = ax.plot([], [], 'r-', lw=2)
point, = ax.plot([], [], 'bo', markersize=10)
annotation = ax.annotate('', xy=(0, 0), xytext=(-10, 10),
                        textcoords='offset points', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'),
                        arrowprops=dict(arrowstyle="->"))

# Adiciona um círculo para representar o farol
circle = plt.Circle((0, 0), 0.2, color='black', fill=True)
ax.add_patch(circle)

# Cria a animação
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, 120), interval=100, blit=True)

# Exibe a animação
plt.title('Simulação do Movimento do Raio de Luz ao Longo da Praia')
plt.xlabel('Distância ao Longo da Praia (km)')
plt.ylabel('Altura (km)')
plt.grid()
plt.show()
