En el código que has proporcionado, se ha agregado un bucle anidado `for` para recorrer todos los píxeles de la imagen después de imprimir el tamaño y el valor del píxel en la posición (0, 0).

```python
for x in range(0, tamanio[0]):
    for y in range(0, tamanio[1]):
        print(pixeles[x, y])
```

Estos bucles recorren todas las coordenadas de píxeles en la imagen, desde `(0, 0)` hasta `(ancho-1, altura-1)`. En cada iteración, se accede al valor del píxel en la posición `(x, y)` utilizando `pixeles[x, y]` y se imprime.

Este código imprimirá el valor de cada píxel en la imagen, línea por línea, empezando desde la esquina superior izquierda y avanzando hacia la derecha y luego hacia abajo, hasta llegar a la esquina inferior derecha.

Es importante tener en cuenta que la imagen "josevicentepeq.jpg" debe estar en el mismo directorio que el script de Python o proporcionar la ruta completa de la imagen para que se pueda abrir correctamente.