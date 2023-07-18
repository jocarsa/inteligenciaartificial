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
            bajado = recortado.resize((int(tamaniocuadradito/4), int(tamaniocuadradito/4)), Image.LANCZOS)
            bajado.save("../cuadraditosbaja/"+str(identificador)+".jpg")
            print(list(bajado.getdata()))
            identificador += 1

archivoseliminar = os.listdir("../cuadraditosalta/")
for archivo in archivoseliminar:
    os.remove("../cuadraditosalta/"+archivo)
archivoseliminar = os.listdir("../cuadraditosbaja/")
for archivo in archivoseliminar:
    os.remove("../cuadraditosbaja/"+archivo)

archivos = os.listdir("../carasaltaresolucion")
for archivo in archivos:   
    parteEnTrozos("../carasaltaresolucion/"+archivo,32)
