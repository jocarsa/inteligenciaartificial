from PIL import Image, ImageColor
import sqlite3
import numpy as np



def mapeo(value):
    value = max(0, min(255, value))
    mapped_value = (value / 255) * 9
    return mapped_value

imagennueva = Image.new("RGB", (1024, 1024), ImageColor.getrgb("white"))

conn = sqlite3.connect("../upscaler.sqlite")
cursor = conn.cursor()

cursor.execute('SELECT data FROM datos LIMIT 100')
filas = cursor.fetchall()
datos = np.array(filas)
print("cargo la información en la lista")
print(datos)
imagen = Image.open("../pruebabaja.jpg")

for x in range(0,256,8):
    for y in range(0,256,8):
        recortado = imagen.crop((x, y, x+8, y+8))
        pixeles = list(recortado.getdata())
        cadena = ""
        for pixel in pixeles:
            media = (pixel[0]+pixel[1]+pixel[2])/3
            cadena += str(round(mapeo(media)))
        print(cadena)
        mejorcandidatoid = 0
        mejorcandidatosuma = 10000000000
        
        for j in range(0,len(datos)):
            cadenaoriginal = cadena
            cadenadb = datos[j][0]
            suma = 0;
            for i in range(0,len(cadenaoriginal)):
                suma += abs(int(cadenaoriginal[i]) - int(cadenadb[i]))
            if suma < mejorcandidatosuma:
                mejorcandidatosuma = suma
                mejorcandidatoid = j
        print(mejorcandidatoid)
        
        cuadrado = Image.open("../cuadraditosalta/"+str(mejorcandidatoid)+".jpg")
        cuadradotransparencia = cuadrado.copy()
        cuadradotransparencia.putalpha(int(255 * 1))
        imagennueva.paste(cuadradotransparencia, [x*4,y*4],cuadradotransparencia)
        imagennueva.save("resultado.png")
conn.close()
