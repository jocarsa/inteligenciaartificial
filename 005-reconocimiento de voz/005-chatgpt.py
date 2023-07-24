import requests
from gtts import gTTS
import os

def texto_a_voz(texto, idioma='es'):
    # Crea un objeto de la clase gTTS con el texto y el idioma
    tts = gTTS(text=texto, lang=idioma)

    # Guarda el audio en un archivo temporal
    tts.save("audio_temporal.mp3")

    # Reproduce el audio usando el reproductor predeterminado
    os.system("start audio_temporal.mp3")

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

    return response_data['choices'][0]

if __name__ == "__main__":
    prompt = "¿Se permite la herencia múltiple en Python?"
    chat_response = get_chat_response(prompt)
    print("ChatGPT:", texto_a_voz(chat_response['message']['content']))
