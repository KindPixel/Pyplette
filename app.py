from scripts.audio_tools import *
from scripts.whisper_tools import *
from scripts.ai_tools import *

# Record and transcribe
audio_filename = "./sounds/output.wav"

# record_audio(audio_filename)

# transcribed_text = transcribe_audio(audio_filename)
# print("Transcribed text:", transcribed_text)

# response = chat_with_gemini("Quelle est la voiture la plus chère du monde ?")
# response = chat_with_gpt("Quelle est la voiture la plus chère du monde ?")
prompt = "Tell me a story about a brave knight."
model = "roberta-large"  # Utilise un modèle approprié pour la génération de texte
response = generate_text_huggingface(prompt, model)
if isinstance(response, list) and 'generated_text' in response[0]:
    generated_text = response[0]['generated_text']
    print("Generated text:", generated_text)
else:
    print("Response:", response)