from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import math
import numpy as np
import cv2
from collections import Counter

def reduce_angle(angle):
    angle %= 360  # Map the angle to the range 0 to 360 degrees

    if angle <= -180:
        angle += 360
    elif angle > 180:
        angle -= 360

    # Round the angle to the nearest multiple of 45 degrees
    reduced_angle = round(angle / 45) * 45

    return reduced_angle

def calculaAngulo(imagen):
    image = imagen  # Replace with your image file name
    gray_image = image.convert("L")
    image_array = np.array(gray_image)
    edges = cv2.Canny(image_array, threshold1=30, threshold2=100)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    x1, y1, x2, y2 = cv2.boundingRect(largest_contour)
    delta_x = x2 - x1
    delta_y = y2 - y1
    angle_rad = np.arctan2(delta_y, delta_x)
    angle_deg = np.degrees(angle_rad)
    return angle_deg

def convert_to_percentage(values):
    total = sum(values)
    percentages = [(value / total) * 100 for value in values]
    return percentages

def hsl_to_rgb(h, s, l):
    h /= 360.0
    s /= 100.0
    l /= 100.0

    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1/6:
                return p + (q - p) * 6 * t
            if t < 1/2:
                return q
            if t < 2/3:
                return p + (q - p) * (2/3 - t) * 6
            return p

        if l < 0.5:
            q = l * (1 + s)
        else:
            q = l + s - l * s

        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)

    r = int(round(r * 255))
    g = int(round(g * 255))
    b = int(round(b * 255))

    return r, g, b

def convert_dict_values_to_percentage(dictionary, decimal_places=2):
    total = sum(dictionary.values())
    percentages = {key: round((value / total) * 100, decimal_places) for key, value in dictionary.items()}
    return percentages

imagen = Image.open("josevicentepeq.jpg")
imagengris = imagen.convert("L")
bordes = imagengris.filter(ImageFilter.FIND_EDGES)
enhancer = ImageEnhance.Contrast(bordes)
contrast_factor = 2.0
enhanced_image = enhancer.enhance(contrast_factor)
pixeles = imagen.load()
tamanio = imagen.size
anchura = tamanio[0]
altura = tamanio[1]
print(tamanio)


anchuradestino = int(anchura)  
alturadestino = int(altura)  
color = (0,0,0)
anchurarectangulo = 4
imagendestino = Image.new('RGB', (anchuradestino, alturadestino), color)
dibujo = ImageDraw.Draw(imagendestino)
angulo = 0
radio = 0
lista = []
for i in range(0,3000):
    
    radio += 0.03
    angulo += 0.1
    componentex = round(anchura/2+math.cos(angulo)*radio)
    componentey = round(altura/2+math.sin(angulo)*radio)
    nuevocolor = pixeles[componentex,componentey]
    #print(str(componentex)+","+str(componentey))
    
    
    region = enhanced_image.crop((
        componentex,
        componentey,
        componentex+anchurarectangulo,
        componentey+anchurarectangulo))
    try:
        #print(calculaAngulo(region))
        dibujo.rectangle(
        [(
            componentex,
            componentey
            ),
         (
            componentex+4,
            componentey+4
            )
        ],
        fill=hsl_to_rgb(
            round(calculaAngulo(region)),
            100,50
            ))
        lista.append(reduce_angle(round(calculaAngulo(region))))
    except:
        pass
print(lista)

diccionario = {-180:0,-135:0,-90:0,-45:0,0:0,45:0,90:0,135:0,180:0}

for elemento in lista:
    diccionario[elemento] += 1
print(diccionario)
diccionarioporcentajes = convert_dict_values_to_percentage(diccionario,decimal_places=0)
print(diccionarioporcentajes)

imagendestino.show()












