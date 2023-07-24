import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar recursos necesarios para el análisis de sentimiento
nltk.download('vader_lexicon')

# Crear un objeto SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Texto de ejemplo para análisis de sentimiento
texto_ejemplo = "La vida es bella."

# Realizar el análisis de sentimiento
scores = analyzer.polarity_scores(texto_ejemplo)

# Interpretar los resultados
print("Texto de ejemplo:", texto_ejemplo)
print("Puntuación de sentimiento:", scores['compound'])

# Interpretar el sentimiento
print(scores)
if scores['compound'] >= 0.05:
    print("Sentimiento: Positivo")
elif scores['compound'] <= -0.05:
    print("Sentimiento: Negativo")
else:
    print("Sentimiento: Neutro")
