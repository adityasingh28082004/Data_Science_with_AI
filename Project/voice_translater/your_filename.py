from playsound3 import playsound
import sounddevice as sd
import soundfile as sf
from pathlib import Path
from faster_whisper import WhisperModel
import asyncio
import edge_tts
import time
import requests
import os


# Save audio files in the same folder as this Python script
folder = Path(__file__).parent
audio_file = folder / "live_input.wav"
output_file = folder / "translated_voice.mp3"

# Recording settings
duration = 8
sample_rate = 16000
microphone_device = 5

# Source name, source code, target name, target code, target voice
languages = {
    "1": ("Hindi", "hi", "Tamil", "ta", "ta-IN-PallaviNeural"),
    "2": ("Tamil", "ta", "Hindi", "hi", "hi-IN-SwaraNeural"),
    "3": ("Hindi", "hi", "English", "en", "en-IN-NeerjaNeural"),
    "4": ("English", "en", "Hindi", "hi", "hi-IN-SwaraNeural"),
    "5": ("Tamil", "ta", "English", "en", "en-IN-NeerjaNeural"),
    "6": ("English", "en", "Tamil", "ta", "ta-IN-PallaviNeural"),
}


# Load speech recognition model
print("Loading speech recognition model...")
start = time.time()

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

print(f"Model loaded in {time.time() - start:.2f} seconds.")


# Translate text using MyMemory API






def translate_text(text, source_code, target_code):
    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source_code}|{target_code}"
    }

    try:
        response = requests.get(url, params=params, timeout=20)
        print("MyMemory HTTP status:", response.status_code)

        response.raise_for_status()
        data = response.json()

        if data.get("responseStatus") != 200:
            print("Translation service message:",
                  data.get("responseDetails", "Unknown error"))
            return ""

        translated_text = (
            data.get("responseData", {})
                .get("translatedText", "")
                .strip()
        )

        if not translated_text:
            print("No translated text returned.")
            return ""

        return translated_text

    except requests.exceptions.RequestException as error:
        print("MyMemory connection error:", error)
        return ""
    except (ValueError, AttributeError, TypeError) as error:
        print("Unexpected translation response:", error)
        return ""




# Generate translated speech
async def generate_voice(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(output_file))



# Main program
while True:
    print("\n========== LANGUAGE TRANSLATOR ==========")
    print("1. Hindi to Tamil")
    print("2. Tamil to Hindi")
    print("3. Hindi to English")
    print("4. English to Hindi")
    print("5. Tamil to English")
    print("6. English to Tamil")
    print("7. Exit")

    choice = input("Choose an option (1-7): ").strip()

    if choice == "7":
        print("Translator stopped.")
        break

    if choice not in languages:
        print("Invalid choice. Please select 1 to 7.")
        continue

    (
        source_name,
        source_code,
        target_name,
        target_code,
        voice
    ) = languages[choice]

    print(f"\nSelected: {source_name} to {target_name}")

    while True:
        print(f"\nSpeak in {source_name} for {duration} seconds...")

        try:
            # Record microphone audio
            audio = sd.rec(
                int(duration * sample_rate),
                samplerate=sample_rate,
                channels=1,
                dtype="float32",
                device=microphone_device
            )

            sd.wait()

            sf.write(
                str(audio_file),
                audio,
                sample_rate
            )

            print("Recording completed!")

           
            # Convert speech to text
            start = time.time()

            segments, info = model.transcribe(
                str(audio_file),
                language=source_code,
                vad_filter=True,
                condition_on_previous_text=False,
                beam_size=3,
                temperature=0.0,
            )

            source_text = " ".join(
                segment.text.strip() for segment in segments
            ).strip()

            recognition_time = time.time() - start
            print(f"Recognition took {recognition_time:.2f} seconds.")
            print(f"\nRecognized {source_name}:")
            print(source_text if source_text else "No speech recognized.")

            if not source_text:
                print("Please speak clearly and try again.")
            else:
                # Translate recognized speech
                start = time.time()
                print("Text sent for translation:", repr(source_text))
                print("Language pair:", source_code, "->", target_code)

                translated_text = translate_text(
                    source_text,
                    source_code,
                    target_code
                )

               
                if not translated_text:
                    print(
                        "Translation returned no text. Please try again."
                    )

                else:
                    print(f"\nTranslated {target_name}:")
                    print(translated_text)

                    print(
                        f"Translation took {time.time() - start:.2f} seconds."
                    )

                    # Generate translated voice
                    
                    start = time.time()

                    asyncio.run(generate_voice(translated_text, voice))

                    voice_time = time.time() - start
                    print(f"Voice generation took {voice_time:.2f} seconds.")

                     # Play translated voice
                    playsound(str(output_file), block=True)
                    print("Translated voice played successfully!")

        except Exception as error:
            print("\nAn error occurred:", error)
            print(
                "Check your internet connection, translation service, "
                "and voice settings."
            )

        repeat = input(
            "\nPress Enter to record again, type m for language menu, "
            "or q to quit: "
        ).strip().lower()

        if repeat == "q":
            print("Translator stopped.")
            raise SystemExit

        if repeat == "m":
            break
