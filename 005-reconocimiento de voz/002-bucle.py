import speech_recognition as sr

def reconocer_voz():
    # Crea un objeto de reconocimiento de voz
    reconocimiento = sr.Recognizer()

    # Utiliza el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        audio = reconocimiento.listen(source)

    try:
        # Intenta reconocer el discurso utilizando el motor de reconocimiento de Google
        texto = reconocimiento.recognize_google(audio, language="es-ES")
        print("Has dicho: " + texto)
    except sr.UnknownValueError:
        print("No se pudo entender el discurso")
    except sr.RequestError as e:
        print("Error al solicitar los resultados; {0}".format(e))
    reconocer_voz()

if __name__ == "__main__":
    reconocer_voz()
