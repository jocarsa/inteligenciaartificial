import requests
from gtts import gTTS
import os
import speech_recognition as sr

def reconocer_voz():
    # Crea un objeto de reconocimiento de voz
    reconocimiento = sr.Recognizer()

    # Utiliza el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        audio = reconocimiento.listen(source)
        reconocimiento.adjust_for_ambient_noise(source, duration=1)

    try:
        # Intenta reconocer el discurso utilizando el motor de reconocimiento de Google
        texto = reconocimiento.recognize_google(audio, language="es-ES")
        print("Has dicho: " + texto)
        prompt = texto
        chat_response = get_chat_response(prompt)
        print("ChatGPT:", texto_a_voz(chat_response['message']['content']))
    except sr.UnknownValueError:
        print("No se pudo entender el discurso")
    except sr.RequestError as e:
        print("Error al solicitar los resultados; {0}".format(e))

def texto_a_voz(texto, idioma='es'):
    # Crea un objeto de la clase gTTS con el texto y el idioma
    tts = gTTS(text=texto, lang=idioma)

    # Guarda el audio en un archivo temporal
    tts.save("audio_temporal.mp3")

    # Reproduce el audio usando el reproductor predeterminado
    os.system("start audio_temporal.mp3")

def get_chat_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    api_key = ""  # Reemplaza esto con tu clave de API de OpenAI

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    print(response_data)
    return response_data['choices'][0]

if __name__ == "__main__":
    reconocer_voz()
    
