from PIL import Image
 
imagen = Image.open("josevicentepeq.jpg")
pixeles = imagen.load()
tamanio = imagen.size
print(tamanio)
print(pixeles[0,0])
for x in range(0,tamanio[0]):
    for y in range(0,tamanio[1]):
        print(pixeles[x,y])


