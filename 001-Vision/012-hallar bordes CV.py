from PIL import Image, ImageDraw, ImageFilter
import math
import numpy as np
import cv2

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
 
imagen = Image.open("josevicentepeq.jpg")
imagengris = imagen.convert("L")
bordes = imagengris.filter(ImageFilter.FIND_EDGES)
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
for i in range(0,3000):
    radio += 0.03
    angulo += 0.1
    componentex = round(anchura/2+math.cos(angulo)*radio)
    componentey = round(altura/2+math.sin(angulo)*radio)
    nuevocolor = pixeles[componentex,componentey]
    #print(str(componentex)+","+str(componentey))
    dibujo.point(
        (
            componentex,
            componentey
        ),
        fill=nuevocolor)
    region = bordes.crop((
        componentex,
        componentey,
        componentex+anchurarectangulo,
        componentey+anchurarectangulo))
    try:
        print(calculaAngulo(region))
    except:
        pass
    imagendestino.paste(region, (
        componentex,
        componentey,
        componentex+anchurarectangulo,
        componentey+anchurarectangulo))
imagendestino.show()
