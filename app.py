from flask import Flask, send_file
from PIL import Image, ImageDraw
import numpy as np
import os

app = Flask(__name__)

def crear_ramo_lirios(cantidad_lirios=5):
    # Crear una imagen en blanco
    ancho, alto = 800, 800
    imagen = Image.new('RGB', (ancho, alto), (255, 255, 255))
    dibujar = ImageDraw.Draw(imagen)

    # Definir los colores para los lirios amarillos y los tallos
    color_lirio = (255, 215, 0)  # Amarillo dorado
    color_tallo = (34, 139, 34)   # Verde
    color_fondo = (255, 250, 240) # Fondo crema

    # Dibujar el fondo
    dibujar.rectangle([0, 0, ancho, alto], fill=color_fondo)

    # Posiciones y tamaños para los lirios
    posiciones = np.linspace(300, 500, cantidad_lirios)
    radio_lirios = 30  # Radio más pequeño para los lirios
    distancia_tallos = 60  # Distancia entre los tallos

    # Dibujar los lirios y tallos
    for i, pos in enumerate(posiciones):
        # Posiciones para los lirios
        x = pos
        y = 300 + (np.random.randint(-10, 10))  # Añadir algo de aleatoriedad en la posición Y

        # Dibujar un lirio (forma más compleja)
        dibujar.polygon([(x, y), (x - radio_lirios, y - radio_lirios), (x + radio_lirios, y - radio_lirios)],
                         fill=color_lirio)
        dibujar.polygon([(x, y), (x - radio_lirios, y + radio_lirios), (x + radio_lirios, y + radio_lirios)],
                         fill=color_lirio)

        # Dibujar un tallo verde
        dibujar.line([x, y, x, 700], fill=color_tallo, width=5)

        # Añadir detalles de hojas
        dibujar.ellipse([x - 15, 400, x + 15, 430], fill=(0, 100, 0))

    # Guardar la imagen en formato PNG
    imagen.save('lirios_ramo.png')
    return 'lirios_ramo.png'

@app.route('/')
def mostrar_imagen():
    nombre_archivo = crear_ramo_lirios(7)
    response = send_file(nombre_archivo, mimetype='image/png')
    os.remove(nombre_archivo)  # Eliminar el archivo después de enviarlo
    return response

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")




if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

