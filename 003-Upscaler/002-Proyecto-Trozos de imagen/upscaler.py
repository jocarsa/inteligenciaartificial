from PIL import Image
import os

imagen = Image.open("../carasaltaresolucion/cara0.jpg")
tamanio = imagen.size
print(tamanio)
anchura = tamanio[0]
altura = tamanio[1]
cuadradito = 64
for x in range(0,anchura,cuadradito):
    for y in range(0,altura,cuadradito):
        recortado = imagen.crop((x, y, x+cuadradito, y+cuadradito))
        recortado.save("../cuadraditosalta/cara0-"+str(x)+"-"+str(y)+".jpg")
