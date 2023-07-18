from PIL import Image


def mapeo(value):
    value = max(0, min(255, value))
    mapped_value = (value / 255) * 9
    return mapped_value


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
