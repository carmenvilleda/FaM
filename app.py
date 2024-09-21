from flask import Flask, send_file
from PIL import Image, ImageDraw
import numpy as np
import os

app = Flask(__name__)

def crear_ramo_flores(cantidad_flores=45):
    # Crear una imagen con fondo rosa pálido
    ancho, alto = 800, 800
    imagen = Image.new('RGB', (ancho, alto), (255, 192, 203))  # Fondo rosa pálido
    dibujar = ImageDraw.Draw(imagen)

    # Colores
    color_lirio = (255, 255, 102)  # Amarillo suave
    color_borde = (255, 140, 0)     # Naranja claro
    color_tallo = (34, 139, 34)     # Verde
    color_hoja = (0, 128, 0)        # Verde oscuro

    # Espaciado y ángulo para la distribución espiral
    angulo = np.linspace(0, 6 * np.pi, cantidad_flores)
    radio = np.linspace(50, 250, cantidad_flores)

    # Dibujar las flores
    for i in range(cantidad_flores):
        # Calcular la posición de cada flor
        x = 400 + radio[i] * np.cos(angulo[i])
        y = 400 + radio[i] * np.sin(angulo[i])

        # Dibujar pétalos con diferentes formas
        for angle in range(0, 360, 30):
            petalo_x = x + 40 * np.cos(np.radians(angle))
            petalo_y = y + 40 * np.sin(np.radians(angle))

            petalo_ancho = 20 + np.random.randint(-5, 5)
            petalo_largo = 40 + np.random.randint(-5, 5)

            dibujar.ellipse([petalo_x - petalo_ancho, petalo_y - petalo_largo, petalo_x + petalo_ancho, petalo_y + 5], fill=color_lirio)
            dibujar.ellipse([petalo_x - petalo_ancho - 2, petalo_y - petalo_largo - 2, petalo_x + petalo_ancho + 2, petalo_y + 7], outline=color_borde, width=2)

        # Solo algunos tallos
        if i % 2 == 0:  # Cada segunda flor tendrá tallo
            dibujar.line([x, y + 5, 400, 700], fill=color_tallo, width=8)

        # Dibujar el centro de la flor
        centro_color = (255, 204, 0)
        dibujar.ellipse([x - 15, y - 15, x + 15, y + 15], fill=centro_color)

        # Dibujar hojas
        hoja_ancho = 30
        hoja_largo = 50
        hoja_offset = np.random.randint(-10, 10)
        dibujar.polygon([(x - 25, y + 5), (x - hoja_ancho + hoja_offset, y + hoja_largo), (x, y + 10)], fill=color_hoja)  # Hoja izquierda
        dibujar.polygon([(x + 25, y + 5), (x + hoja_ancho + hoja_offset, y + hoja_largo), (x, y + 10)], fill=color_hoja)  # Hoja derecha

    # Guardar la imagen en formato PNG
    imagen.save('ramo_flores.png')
    return 'ramo_flores.png'

@app.route('/')
def mostrar_imagen():
    nombre_archivo = crear_ramo_flores(45)
    response = send_file(nombre_archivo, mimetype='image/png')
    os.remove(nombre_archivo)
    return response

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

