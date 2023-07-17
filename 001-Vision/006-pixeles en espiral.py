from PIL import Image, ImageDraw
import math
 
imagen = Image.open("josevicentepeq.jpg")
pixeles = imagen.load()
tamanio = imagen.size
anchura = tamanio[0]
altura = tamanio[1]
print(tamanio)


anchuradestino = int(anchura)  
alturadestino = int(altura)  
color = (255, 255, 255)

imagendestino = Image.new('RGB', (anchuradestino, alturadestino), color)
dibujo = ImageDraw.Draw(imagendestino)
angulo = 0
radio = 0
for i in range(0,5000):
    radio += 0.03
    angulo += 0.1
    dibujo.point(
        (
            anchura/2+math.cos(angulo)*radio,
            altura/2+math.sin(angulo)*radio
        ),
        fill=(255,0,0))
imagendestino.show()
