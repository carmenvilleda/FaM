from flask import Flask, send_file
from PIL import Image, ImageDraw
import numpy as np

app = Flask(__name__)

# Función para crear una imagen de un ramo de lirios amarillos
def crear_ramo_lirios(cantidad_lirios=5):
    # Crear una imagen en blanco
    imagen = Image.new('RGB', (800, 800), (255, 255, 255))
    dibujar = ImageDraw.Draw(imagen)

    # Definir los colores para los lirios amarillos y los tallos
    color_lirio = (255, 255, 0)
    color_tallo = (34, 139, 34)
    
    # Posiciones y tamaños para los lirios
    posiciones = np.linspace(100, 700, cantidad_lirios)
    radio_lirios = 50
    
    # Dibujar los lirios
    for pos in posiciones:
        # Dibujar un círculo amarillo para representar el lirio
        dibujar.ellipse([pos-radio_lirios, 300-radio_lirios, pos+radio_lirios, 300+radio_lirios], fill=color_lirio)
        
        # Dibujar un tallo verde
        dibujar.line([pos, 300, pos, 700], fill=color_tallo, width=5)
    
    # Guardar la imagen en formato PNG
    imagen.save('lirios_ramo.png')
    return 'lirios_ramo.png'

# Ruta principal de la app
@app.route('/')
def mostrar_imagen():
    nombre_archivo = crear_ramo_lirios(7)
    return send_file(nombre_archivo, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

