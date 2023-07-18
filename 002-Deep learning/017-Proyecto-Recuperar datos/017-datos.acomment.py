En el código proporcionado, se han realizado los siguientes cambios:

1. Se ha importado la clase `Counter` del módulo `collections` para contar la frecuencia de los ángulos calculados.
2. Se ha agregado una lista vacía `lista` antes del bucle `for`. Esta lista se utiliza para almacenar los ángulos calculados en cada iteración.
3. Dentro del bucle `for`, se ha añadido el ángulo redondeado `round(calculaAngulo(region))` a la lista `lista` utilizando `lista.append()`.
4. Después del bucle `for`, se imprime la lista completa de ángulos almacenados.
5. Se utiliza la clase `Counter` para contar la frecuencia de los ángulos en la lista `lista`. Se obtiene el recuento total y se almacenan los valores y sus respectivas frecuencias en las variables `labels` y `sizes`.
6. Se itera sobre los elementos de `counter` ordenados por frecuencia descendente y se calcula el porcentaje correspondiente a cada ángulo.
7. Finalmente, se imprime el número de ángulo y su porcentaje correspondiente.

Estos cambios permiten obtener la frecuencia y el porcentaje de aparición de los ángulos calculados en la lista `lista`.