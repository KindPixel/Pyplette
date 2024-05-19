import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
import time

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Initialisation du client OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def chat_with_gpt(transcription):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": transcription,
            }
        ],
        model="gpt-3.5-turbo",  # Ou "gpt-4" selon votre abonnement
    )
    return chat_completion.choices[0].message['content']


def chat_with_gemini(prompt):
    api_key = os.getenv('GOOGLE_API_KEY')
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print(response.text)
        return "Failed to get a response from the API."


def generate_text_huggingface(prompt, model):
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {
        "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt
    }

    while True:
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result
        elif response.status_code == 503 and 'estimated_time' in response.json():
            wait_time = response.json()['estimated_time']
            print(f"Model is currently loading. Estimated time: {wait_time} seconds")
            time.sleep(wait_time + 5)  # Ajouter un petit délai supplémentaire pour garantir que le modèle est prêt
        else:
            response.raise_for_status()  # Raise an HTTPError for other bad responses (4xx and 5xx)
