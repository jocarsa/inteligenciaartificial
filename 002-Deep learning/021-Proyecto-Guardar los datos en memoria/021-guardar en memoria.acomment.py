En el código proporcionado, se han realizado los siguientes cambios:

1. Se ha importado el módulo `numpy` con el alias `np`.
2. Se ha agregado la importación del módulo `cv2` para utilizar funciones relacionadas con la manipulación de imágenes.
3. Se ha agregado la importación de la clase `Counter` del módulo `collections`.
4. Se ha definido una función llamada `reduce_angle` que toma un ángulo en grados y lo reduce al rango de 0 a 360 grados. Si el ángulo es menor o igual a -180, se suma 360. Si el ángulo es mayor a 180, se resta 360. Luego, se redondea el ángulo al múltiplo de 45 grados más cercano.
5. Se ha agregado una función llamada `convert_dict_values_to_percentage` que toma un diccionario y convierte los valores en porcentajes. Toma un diccionario como entrada y devuelve un nuevo diccionario con los valores convertidos a porcentajes.
6. Se ha agregado una impresión de las dimensiones de la imagen (`tamanio`) para mostrar su tamaño.
7. Se ha agregado un bloque `try-except` para capturar posibles excepciones al calcular el ángulo utilizando la función `calculaAngulo`.
8. Se ha agregado una lista llamada `lista` para almacenar los ángulos reducidos.
9. Se ha agregado un bucle `for` que itera 3000 veces para generar puntos en una circunferencia y calcular los ángulos correspondientes. Luego, se agrega el ángulo reducido a la lista `lista`.
10. Se ha inicializado un diccionario llamado `diccionario` con claves predefinidas que representan los ángulos reducidos y valores iniciales en cero.
11. Se ha agregado un bucle `for elemento in lista` para recorrer la lista `lista` y actualizar los valores del diccionario `diccionario` según el conteo de cada ángulo reducido.
12. Se ha agregado una impresión del diccionario `diccionario` para mostrar los conteos de cada ángulo reducido.
13. Se ha llamado a la función `convert_dict_values_to_percentage` para convertir los valores del diccionario `diccionario` en porcentajes y se ha almacenado el resultado en el diccionario `diccionarioporcentajes`.
14. Se ha abierto un archivo de texto llamado "memoria.txt" en modo de apendizaje ("a") y se ha escrito el contenido del diccionario `diccionarioporcentajes` en una nueva línea.
15. Se ha cerrado el archivo de texto.
16. Se ha mostrado la imagen resultante utilizando el método `show()`.

Estos cambios agregan funcionalidad para calcular los porcentajes de cada ángulo reducido y guardar los resultados en un archivo de texto.