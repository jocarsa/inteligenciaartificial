from PIL import Image
import os
import sqlite3
identificador = 0

conn = sqlite3.connect("../upscaler.sqlite")
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos (
            id INTEGER PRIMARY KEY,
            data TEXT
        )
    ''')

def mapeo(value):
    value = max(0, min(255, value))
    mapped_value = (value / 255) * 9
    return mapped_value

def parteEnTrozos(imagenorigen,tamaniocuadradito):
    global identificador
    global conn
    global cursor
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
            #bajado.save("../cuadraditosbaja/"+str(identificador)+".jpg")
            pixeles = list(bajado.getdata())
            cadena = ""
            for pixel in pixeles:
                media = (pixel[0]+pixel[1]+pixel[2])/3
                cadena += str(round(mapeo(media)))
            #print(cadena)
            cursor.execute('INSERT INTO datos VALUES ('+str(identificador)+',"'+cadena+'");')
            identificador += 1
    conn.commit()
    

archivoseliminar = os.listdir("../cuadraditosalta/")
for archivo in archivoseliminar:
    os.remove("../cuadraditosalta/"+archivo)
archivoseliminar = os.listdir("../cuadraditosbaja/")
for archivo in archivoseliminar:
    os.remove("../cuadraditosbaja/"+archivo)

archivos = os.listdir("../carasaltaresolucion")
for archivo in archivos:   
    parteEnTrozos("../carasaltaresolucion/"+archivo,32)

conn.close()
