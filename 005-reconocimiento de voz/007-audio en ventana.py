import requests
from gtts import gTTS
import os
import speech_recognition as sr
import tkinter as tk
import pygame

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
        #print("ChatGPT:", texto_a_voz(chat_response['message']['content']))
    # Play the audio in a tkinter window
        root = tk.Tk()
        root.title("ChatGPT Response")

        label = tk.Label(root, text="ChatGPT Response:")
        label.pack()

        texto_a_voz(chat_response['message']['content'])

        root.mainloop()

    except sr.UnknownValueError:
        print("No se pudo entender el discurso")
    except sr.RequestError as e:
        print("Error al solicitar los resultados; {0}".format(e))

def texto_a_voz(texto, idioma='es'):
    # Crea un objeto de la clase gTTS con el texto y el idioma
    tts = gTTS(text=texto, lang=idioma)

    # Guarda el audio en un archivo temporal
    tts.save("audio_temporal.mp3")

    # Reproduce el audio usando pygame
    pygame.mixer.init()
    pygame.mixer.music.load("audio_temporal.mp3")
    pygame.mixer.music.play()

    # Espera a que termine de reproducirse el audio
    while pygame.mixer.music.get_busy():
        continue

def get_chat_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    api_key = "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"  # Reemplaza esto con tu clave de API de OpenAI

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
    
