from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def draw_flower():
    fig, ax = plt.subplots()

    # Crear el tallo de la flor
    stem_x = np.linspace(0, 0, 100)
    stem_y = np.linspace(0, 1, 100)
    ax.plot(stem_x, stem_y, color='green', lw=2)

    # Crear pétalos
    theta = np.linspace(0, 2 * np.pi, 100)
    for angle in np.linspace(0, 2 * np.pi, 6):
        petal_x = 0.2 * np.cos(theta) + np.cos(angle)
        petal_y = 0.2 * np.sin(theta) + np.sin(angle) + 1
        ax.fill(petal_x, petal_y, color='yellow')

    # Crear el centro de la flor
    center_x = 0.1 * np.cos(theta)
    center_y = 0.1 * np.sin(theta) + 1
    ax.fill(center_x, center_y, color='white')

    # Crear hojas
    leaf_theta = np.linspace(0, np.pi, 100)
    leaf_x = 0.2 * np.cos(leaf_theta) - 0.2
    leaf_y = 0.1 * np.sin(leaf_theta) + 0.5
    ax.fill(leaf_x, leaf_y, color='blue')

    leaf_x2 = 0.2 * np.cos(leaf_theta) + 0.2
    leaf_y2 = 0.1 * np.sin(leaf_theta) + 0.3
    ax.fill(leaf_x2, leaf_y2, color='blue')

    # Ajustar los límites y ocultar los ejes
    ax.set_xlim([-1, 1])
    ax.set_ylim([0, 1.5])
    ax.axis('off')

    # Guardar la imagen temporalmente
    plt.savefig('/tmp/flower_image.png')
    plt.close(fig)

@app.route('/')
def home():
    draw_flower()
    return send_file('/tmp/flower_image.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
