from PIL import Image, ImageColor
import sqlite3



def mapeo(value):
    value = max(0, min(255, value))
    mapped_value = (value / 255) * 9
    return mapped_value

imagennueva = Image.new("RGB", (1024, 1024), ImageColor.getrgb("white"))

conn = sqlite3.connect("../upscaler.sqlite")
cursor = conn.cursor()

imagen = Image.open("../pruebabaja.jpg")

for x in range(64,192,8):
    for y in range(64,192,8):
        recortado = imagen.crop((x, y, x+8, y+8))
        pixeles = list(recortado.getdata())
        cadena = ""
        for pixel in pixeles:
            media = (pixel[0]+pixel[1]+pixel[2])/3
            cadena += str(round(mapeo(media)))
        print(cadena)
        mejorcandidatoid = 0
        mejorcandidatosuma = 10000000000
        cursor.execute('SELECT * FROM datos')
        filas = cursor.fetchall()
        for fila in filas:
            cadenaoriginal = cadena
            cadenadb = fila[1]
            suma = 0;
            for i in range(0,len(cadenaoriginal)):
                suma += abs(int(cadenaoriginal[i]) - int(cadenadb[i]))
            if suma < mejorcandidatosuma:
                mejorcandidatosuma = suma
                mejorcandidatoid = fila[0]
        print(mejorcandidatoid)
        cuadrado = Image.open("../cuadraditosalta/"+str(mejorcandidatoid)+".jpg")
        imagennueva.paste(cuadrado, [x*4,y*4])
        imagennueva.show()
conn.close()
