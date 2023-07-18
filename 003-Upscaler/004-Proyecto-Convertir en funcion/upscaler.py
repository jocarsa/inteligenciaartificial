from PIL import Image
import os

identificador = 0

def parteEnTrozos(imagenorigen,tamaniocuadradito):
    global identificador
    imagen = Image.open(imagenorigen)
    tamanio = imagen.size
    print(tamanio)
    anchura = tamanio[0]
    altura = tamanio[1]
    cuadradito = tamaniocuadradito

    for x in range(0,anchura,cuadradito):
        for y in range(0,altura,cuadradito):
            recortado = imagen.crop((x, y, x+cuadradito, y+cuadradito))
            recortado.save("../cuadraditosalta/"+str(identificador)+".jpg")
            identificador += 1


parteEnTrozos("../carasaltaresolucion/cara1.jpg",32)
