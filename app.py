from flask import Flask, send_file
from PIL import Image, ImageDraw
import numpy as np
import os

app = Flask(__name__)

def crear_ramo_flores(cantidad_flores=7):
    # Crear una imagen en blanco
    ancho, alto = 800, 800
    imagen = Image.new('RGB', (ancho, alto), (255, 240, 245))  # Fondo rosa pastel
    dibujar = ImageDraw.Draw(imagen)

    # Colores
    color_lirio = (255, 223, 186)  # Amarillo suave
    color_borde = (255, 140, 0)     # Naranja claro
    color_tallo = (34, 139, 34)     # Verde
    color_hoja = (144, 238, 144)    # Verde claro

    # Posiciones y tamaños para las flores
    posiciones = np.linspace(350, 450, cantidad_flores)  # Posiciones centradas
    radio_flores = 40  # Radio de las flores

    # Dibujar las flores
    for pos in posiciones:
        # Posiciones fijas para un ramo
        x = pos
        y = 300 + np.random.randint(-10, 10)

        # Dibujar pétalos con un borde
        for angle in range(0, 360, 30):  # Dibujar 12 pétalos
            petalo_x = x + radio_flores * np.cos(np.radians(angle))
            petalo_y = y + radio_flores * np.sin(np.radians(angle))

            # Pétalo con borde
            dibujar.ellipse([petalo_x - 20, petalo_y - 40, petalo_x + 20, petalo_y + 5], fill=color_lirio)
            dibujar.ellipse([petalo_x - 22, petalo_y - 42, petalo_x + 22, petalo_y + 7], outline=color_borde, width=2)

        # Dibujar el centro de la flor
        centro_color = (255, 255, 102)  # Amarillo claro
        dibujar.ellipse([x - 15, y - 15, x + 15, y + 15], fill=centro_color)  # Centro amarillo claro

        # Dibujar el tallo
        dibujar.line([x, y + 5, x, 700], fill=color_tallo, width=8)

        # Dibujar hojas
        hoja_y1 = y + 30  # Hojas cerca de la flor
        hoja_y2 = hoja_y1 + 30
        dibujar.ellipse([x - 30, hoja_y1, x + 10, hoja_y2], fill=color_hoja)  # Hoja a la izquierda
        dibujar.ellipse([x - 10, hoja_y1, x + 30, hoja_y2], fill=color_hoja)  # Hoja a la derecha

    # Guardar la imagen en formato PNG
    imagen.save('ramo_flores.png')
    return 'ramo_flores.png'

@app.route('/')
def mostrar_imagen():
    nombre_archivo = crear_ramo_flores(7)
    response = send_file(nombre_archivo, mimetype='image/png')
    os.remove(nombre_archivo)  # Eliminar el archivo después de enviarlo
    return response

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
