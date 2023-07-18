from PIL import Image, ImageColor
import sqlite3
import numpy as np
import matplotlib.pyplot as plt


def mapeo(value):
    value = max(0, min(255, value))
    mapped_value = (value / 255) * 9
    return mapped_value

imagennueva = Image.new("RGB", (1024, 1024), ImageColor.getrgb("white"))

conn = sqlite3.connect("../upscaler.sqlite")
cursor = conn.cursor()
total = 256*256
contador = 0
cursor.execute('SELECT data FROM datos')
filas = cursor.fetchall()
datos = np.array(filas)
print("cargo la información en la lista")
print(datos)
imagen = Image.open("../pruebabaja.jpg")

plt.figure()
plt.imshow(imagennueva)

for x in range(0,256,8):
    for y in range(0,256,8):
        contador += 1
        if contador % 100 == 0:
            print(str((contador/total)*100)+"%")
        recortado = imagen.crop((x, y, x+8, y+8))
        pixeles = list(recortado.getdata())
        cadena = ""
        for pixel in pixeles:
            media = (pixel[0]+pixel[1]+pixel[2])/3
            cadena += str(round(mapeo(media)))
        #print(cadena)
        mejorcandidatoid = 0
        mejorcandidatosuma = 10000000000
        
        for j in range(0,len(datos)):
            cadenaoriginal = cadena
            cadenadb = datos[j][0]
            
            suma =  sum(abs(int(digit1) - int(digit2)) for digit1, digit2 in zip(cadenaoriginal, cadenadb))
            if suma < mejorcandidatosuma:
                mejorcandidatosuma = suma
                mejorcandidatoid = j
        #print(mejorcandidatoid)
        
        cuadrado = Image.open("../cuadraditosalta/"+str(mejorcandidatoid)+".jpg")
        cuadradotransparencia = cuadrado.copy()
        cuadradotransparencia.putalpha(int(255 * 1))
        imagennueva.paste(cuadradotransparencia, [x*4,y*4],cuadradotransparencia)
        imagennueva.save("resultado.png")
        plt.clf()  
        plt.imshow(imagennueva)
        plt.pause(0.01)
conn.close()
