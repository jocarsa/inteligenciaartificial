from gtts import gTTS
import os

def texto_a_voz(texto, idioma='es'):
    # Crea un objeto de la clase gTTS con el texto y el idioma
    tts = gTTS(text=texto, lang=idioma)

    # Guarda el audio en un archivo temporal
    tts.save("audio_temporal.mp3")

    # Reproduce el audio usando el reproductor predeterminado
    os.system("start audio_temporal.mp3")

if __name__ == "__main__":
    texto = "¡Hola! Soy Jose en el curso de Python y esto es una prueba."
    texto_a_voz(texto)
