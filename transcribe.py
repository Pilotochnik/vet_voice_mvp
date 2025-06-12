import whisper

def transcribe_audio(audio_path):
    print("Обработка аудио...")
    model = whisper.load_model("small")
    result = model.transcribe(audio_path, language="ru")

    print("\n--- Расшифрованный текст ---\n")
    print(result["text"])

    return result["text"]
