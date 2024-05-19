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
response = chat_with_huggingface("Quelle est la voiture la plus chère du monde ?")


print("Chat response:", response)