from PIL import Image
import sqlite3

def mapeo(value):
    value = max(0, min(255, value))
    mapped_value = (value / 255) * 9
    return mapped_value

conn = sqlite3.connect("../upscaler.sqlite")
cursor = conn.cursor()

imagen = Image.open("../pruebabaja.jpg")

for x in range(0,256,8):
    for y in range(0,256,8):
        recortado = imagen.crop((x, y, x+8, y+8))
        pixeles = list(recortado.getdata())
        cadena = ""
        for pixel in pixeles:
            media = (pixel[0]+pixel[1]+pixel[2])/3
            cadena += str(round(mapeo(media)))
        #print(cadena)
        cursor.execute('SELECT * FROM datos WHERE data = "'+cadena+'" LIMIT 1')
        filas = cursor.fetchall()
        for fila in filas:
            print("coincidencia: "+str(fila[0])+" - "+fila[1])

conn.close()
