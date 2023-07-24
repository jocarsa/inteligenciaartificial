import pandas as pd
import nltk
from textblob import TextBlob

# Descargar recursos adicionales de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Función para realizar el análisis de sentimientos
def analisis_sentimientos(texto):
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity

    if polaridad > 0:
        return 'positivo'
    elif polaridad < 0:
        return 'negativo'
    else:
        return 'neutral'

# Ejemplo de comentarios
comentarios = [
    "PHP es horrible.",
    "Java es maravilloso.",
    "Me encanta este producto, es increíble.",
    "No estoy satisfecho con el servicio al cliente.",
    "La comida en este restaurante es deliciosa.",
    "El transporte público es horrible, siempre llega tarde.",
    "No puedo creer lo malo que es este producto.",
    "Hermoso día para disfrutar al aire libre."
]

# Realizar análisis de sentimientos para cada comentario
resultados = []
for comentario in comentarios:
    sentimiento = analisis_sentimientos(comentario)
    resultados.append((comentario, sentimiento))

# Crear un DataFrame para mostrar los resultados
df_resultados = pd.DataFrame(resultados, columns=['Comentario', 'Sentimiento'])
print(df_resultados)
