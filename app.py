from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

app = Flask(_name_)

def draw_flower():
    # Crear una figura y un eje
    fig, ax = plt.subplots(figsize=(6, 8))

    # Fondo negro
    ax.set_facecolor('black')

    # Función para dibujar una flor
    def draw_single_flower(center_x, center_y, petal_color, center_color):
        # Tallo
        ax.plot([center_x, center_x], [center_y - 1, center_y], color='#00FF00', lw=3)

        # Pétalos en círculo
        for angle in np.linspace(0, 2 * np.pi, 6, endpoint=False):
            petal = patches.Ellipse((center_x + 0.3 * np.cos(angle), center_y + 0.3 * np.sin(angle)),
                                    width=0.6, height=1.0, angle=np.degrees(angle),
                                    color=petal_color, ec='none')
            ax.add_patch(petal)

        # Centro de la flor
        center = patches.Circle((center_x, center_y), radius=0.15, color=center_color)
        ax.add_patch(center)

    # Dibujar las tres flores
    draw_single_flower(0, 1.5, '#FFFF00', 'white')   # Flor central
    draw_single_flower(-1.5, 0.5, '#FFFF00', 'white')  # Flor izquierda
    draw_single_flower(1.5, 0.5, '#FFFF00', 'white')   # Flor derecha

    # Hojas en el tallo (lado izquierdo)
    leaf1 = patches.Ellipse((-0.4, 0.5), width=0.8, height=0.3, angle=30, color='#00FF80', ec='none')
    ax.add_patch(leaf1)

    # Hojas en el tallo (lado derecho)
    leaf2 = patches.Ellipse((0.4, 0.6), width=0.8, height=0.3, angle=-30, color='#00FF80', ec='none')
    ax.add_patch(leaf2)

    # Añadir partículas brillantes
    np.random.seed(42)  # Para consistencia en las posiciones
    stars_x = np.random.uniform(-2, 2, 40)
    stars_y = np.random.uniform(-1, 2.5, 40)
    ax.scatter(stars_x, stars_y, color='white', s=10)

    # Configuración de los límites y aspecto
    ax.set_xlim([-2, 2])
    ax.set_ylim([-1, 3])
    ax.axis('off')

    # Guardar la imagen
    plt.savefig('/tmp/flower_image.png', bbox_inches='tight', facecolor='black')
    plt.close(fig)

@app.route('/')
def home():
    draw_flower()
    return send_file('/tmp/flower_image.png', mimetype='image/png')

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
