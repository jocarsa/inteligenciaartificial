from PIL import Image
 
imagen = Image.open("josevicente.jpg")
pixeles = imagen.load()
tamanio = imagen.size
print(tamanio)
print(pixeles[0,0])


