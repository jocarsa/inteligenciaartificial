from PIL import Image, ImageDraw
 
imagen = Image.open("josevicentepeq.jpg")
pixeles = imagen.load()
tamanio = imagen.size
anchura = tamanio[0]/2
altura = tamanio[1]/2
print(tamanio)
print(pixeles[0,0])
print(pixeles[anchura,altura])

anchuradestino = int(anchura)  
alturadestino = int(altura)  
color = (255, 255, 255)

imagendestino = Image.new('RGB', (anchuradestino, alturadestino), color)
dibujo = ImageDraw.Draw(imagendestino)
dibujo.point((50, 50), fill=(255,0,0))
imagendestino.show()
