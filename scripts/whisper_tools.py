import whisper
import warnings

# Désactiver le warning spécifique à FP16
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

def transcribe_audio(filename):
    model = whisper.load_model("small")
    result = model.transcribe(filename, language="fr")
    return result["text"]