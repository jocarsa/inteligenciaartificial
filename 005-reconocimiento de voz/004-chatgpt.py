import requests

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
    print("ChatGPT:", chat_response['message']['content'])
