from PIL import Image
 
imagen = Image.open("josevicentepeq.jpg")
pixeles = imagen.load()
tamanio = imagen.size
anchura = tamanio[0]/2
altura = tamanio[1]/2
print(tamanio)
print(pixeles[0,0])
print(pixeles[anchura,altura])


