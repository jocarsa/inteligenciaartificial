import spacy

# Cargar el modelo en español
nlp = spacy.load('es_core_news_sm')

# Texto de ejemplo para realizar el etiquetado de partes del discurso
texto_ejemplo = "La inteligencia artificial es una rama de la informática que busca desarrollar máquinas capaces de aprender y razonar."

# Procesar el texto con spaCy
doc = nlp(texto_ejemplo)

# Realizar el etiquetado de partes del discurso (POS tagging) y mostrar los resultados
print("Texto de ejemplo:", texto_ejemplo)
for token in doc:
    print(f"Palabra: {token.text}, POS: {token.pos_}, POS detallado: {token.tag_}")
