from openai import OpenAI
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Initialisation du client OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


client = OpenAI()

completion = client.chat.completions.create(
    model="GPT-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

print(completion.choices[0].message)
