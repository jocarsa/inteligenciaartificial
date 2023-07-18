En el código proporcionado, se han realizado los siguientes cambios:

1. Se ha agregado la función `reduce_angle(angle)` para reducir el ángulo calculado a su valor más cercano múltiplo de 45 grados. Esto se logra mapeando el ángulo al rango de 0 a 360 grados, ajustando los valores negativos y redondeando al múltiplo de 45 más cercano.
2. Se ha agregado la función `convert_to_percentage(values)` para convertir los valores en una lista en porcentajes. Se calcula el total de los valores y luego se calcula el porcentaje correspondiente para cada valor en la lista.
3. Se ha modificado la línea donde se almacena el ángulo en la lista `lista` para utilizar la función `reduce_angle` antes de agregar el ángulo a la lista.
4. Se ha añadido una impresión adicional de la lista `lista` para mostrar los ángulos reducidos.
5. Dentro del bucle `for`, se ha utilizado la función `reduce_angle` alrededor de `round(calculaAngulo(region))` antes de pasarlo a `hsl_to_rgb`.
6. Se ha eliminado el segundo conjunto de impresiones de la lista `lista` al final del código, ya que ya se había impreso antes.

Estos cambios permiten reducir los ángulos calculados al múltiplo de 45 más cercano y proporcionar una lista de ángulos reducidos en lugar de los ángulos originales. Además, se ha agregado una función para convertir los valores en porcentajes y se ha realizado una impresión adicional de la lista de ángulos reducidos.