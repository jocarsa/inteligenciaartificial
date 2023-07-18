En el código que has proporcionado, se han agregado las siguientes líneas:

```python
from PIL import ImageDraw

anchuradestino = int(anchura)  
alturadestino = int(altura)  
color = (255, 255, 255)

imagendestino = Image.new('RGB', (anchuradestino, alturadestino), color)
dibujo = ImageDraw.Draw(imagendestino)
dibujo.point((50, 50), fill=(255, 0, 0))
imagendestino.show()
```

En estas líneas, se importa el módulo `ImageDraw` de la biblioteca PIL para poder dibujar en la imagen.

Las variables `anchuradestino` y `alturadestino` se convierten en enteros utilizando la función `int()` para asegurarse de que sean valores enteros y no decimales.

La variable `color` se define como una tupla `(255, 255, 255)`, que representa el color blanco en RGB.

La línea `imagendestino = Image.new('RGB', (anchuradestino, alturadestino), color)` crea una nueva imagen llamada `imagendestino` con el tamaño definido por `anchuradestino` y `alturadestino`. La imagen se inicializa con el color de fondo especificado por `color` (en este caso, blanco).

La línea `dibujo = ImageDraw.Draw(imagendestino)` crea un objeto de dibujo en la imagen `imagendestino`, lo que nos permite realizar operaciones de dibujo en ella.

La línea `dibujo.point((50, 50), fill=(255, 0, 0))` dibuja un punto en las coordenadas `(50, 50)` en la imagen `imagendestino` con el color de relleno especificado por `(255, 0, 0)`, que representa el color rojo en RGB.

Finalmente, la línea `imagendestino.show()` muestra la imagen `imagendestino` en una ventana emergente.

Estas adiciones al código permiten crear una nueva imagen, dibujar un punto rojo en ella y mostrarla en una ventana.