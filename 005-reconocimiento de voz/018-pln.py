import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Descargar los datos requeridos de NLTK (solo necesario una vez)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def nlp_ejemplo(texto):
    # Tokenizar la oración en palabras
    palabras = word_tokenize(texto, language='spanish')

    # Realizar el etiquetado gramatical (POS tagging)
    pos_tags = pos_tag(palabras, lang='es')

    return pos_tags

# Oración de ejemplo
oracion_ejemplo = "La programación informática es muy sencilla."

# Realizar PLN en la oración de ejemplo
resultado = nlp_ejemplo(oracion_ejemplo)

# Mostrar el resultado
print(resultado)
