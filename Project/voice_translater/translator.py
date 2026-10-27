
from faster_whisper import WhisperModel
from pathlib import Path
import requests
import asyncio
import edge_tts

# Find the folder containing this Python file
folder = Path(__file__).parent

# Audio files
hindi_audio = folder / "WhatsApp Audio 2026-10-25 at 7.11.26 AM.mp4"
tamil_audio = folder / "sample_tamil.mp3"


# Convert text into speech
async def generate_speech(text, language):
    if language == "ta":
        voice = "ta-IN-PallaviNeural"
        output_file = folder / "tamil_voice.mp3"
    else:
        voice = "hi-IN-SwaraNeural"
        output_file = folder / "hindi_voice.mp3"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(output_file))

    print("\nVoice generated successfully!")
    print("Audio file:", output_file)


# Translate text using MyMemory
def translate_text(text, source_language, target_language):
    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source_language}|{target_language}"
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()

    if data.get("responseStatus") == 200:
        return data["responseData"]["translatedText"]

    print("Translation failed:", data.get("responseDetails"))
    return None


# Process audio in the selected language
def translate_audio(audio_file, source_language, target_language):
    if not audio_file.exists():
        print("\nAudio file not found:", audio_file)
        return

    print("\nLoading speech recognition model...")

    model = WhisperModel(
        "medium",
        device="cpu",
        compute_type="int8"
    )

    print("Recognizing speech...")

    segments, info = model.transcribe(
        str(audio_file),
        language=source_language,
        vad_filter=True
    )

    recognized_text = " ".join(
        segment.text.strip() for segment in segments
    ).strip()

    print("\nRecognized text:")
    print(recognized_text)

    if not recognized_text:
        print("No speech was recognized.")
        return

    try:
        translated_text = translate_text(
            recognized_text,
            source_language,
            target_language
        )

        if translated_text:
            print("\nTranslated text:")
            print(translated_text)

            asyncio.run(
                generate_speech(translated_text, target_language)
            )

    except requests.RequestException as error:
        print("Translation connection error:", error)

    except Exception as error:
        print("An error occurred:", error)


# Main menu
print("===== AI Hindi-Tamil Translator =====")
print("1. Hindi to Tamil")
print("2. Tamil to Hindi")
print("3. Exit")

choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    translate_audio(hindi_audio, "hi", "ta")

elif choice == "2":
    translate_audio(tamil_audio, "ta", "hi")

elif choice == "3":
    print("Thank you for using the translator!")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
