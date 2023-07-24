import requests
from gtts import gTTS
import os
import speech_recognition as sr
import subprocess
import wave
import pydub

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
   # Save the audio to a temporary file
    temp_mp3_file = "audio_temporal.mp3"
    tts.save(temp_mp3_file)

    # Load the audio from the temporary file
    audio = pydub.AudioSegment.from_file(temp_mp3_file)
    if audio.channels == 1:
        # Convert the audio to stereo by duplicating the mono channel
        audio = audio.set_channels(2)
    # Export the audio as a WAV file
    audio = audio.set_frame_rate(44100)
    wav_file = "audio_temporal.wav"
    audio.export(wav_file, format="wav")

    # Delete the temporary MP3 file
    os.remove(temp_mp3_file)
 
    # Reproduce el audio usando el reproductor predeterminado
    #os.system("start audio_temporal.wav")
    #os.system("./python.exe '014-reproducir wav.py' audio_temporal.wav")
    # Replace 'script_to_execute.py' with the name of the Python script you want to run
    script_to_execute = '016-pantalla completa.py'

    # Replace 'parameter_value' with the actual parameter value you want to pass
    parameter_value = 'audio_temporal.wav'

    # Execute the script with the parameter using subprocess.run
    subprocess.run(['python', script_to_execute, parameter_value])

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
    
