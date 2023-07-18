from PIL import Image
 
imagen = Image.open("josevicente.jpg")
pixeles = imagen.load()
print(pixeles[0,0])


