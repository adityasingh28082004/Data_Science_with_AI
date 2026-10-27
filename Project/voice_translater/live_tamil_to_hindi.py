
import sounddevice as sd
import soundfile as sf
from pathlib import Path
from faster_whisper import WhisperModel
import requests
import asyncio
import edge_tts

# Project folder
folder = Path(__file__).parent

audio_file = folder / "live_tamil_input.wav"
output_file = folder / "live_hindi_voice.mp3"

# Step 1: Record Tamil speech
duration = 5
sample_rate = 16000

print("Speak in Tamil for 5 seconds...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="float32",
    device=5
)

sd.wait()
sf.write(str(audio_file), audio, sample_rate)

print("Recording completed!")

# Step 2: Recognize Tamil speech
print("Recognizing Tamil speech...")

model = WhisperModel(
    "medium",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe(
    str(audio_file),
    language="ta",
    vad_filter=True
)

tamil_text = " ".join(
    segment.text.strip() for segment in segments
).strip()

print("\nRecognized Tamil:")
print(tamil_text if tamil_text else "No speech recognized.")

# Step 3: Translate Tamil into Hindi
if tamil_text:
    try:
        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": tamil_text,
            "langpair": "ta|hi"
        }

        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        response.raise_for_status()
        data = response.json()

        if data.get("responseStatus") == 200:
            hindi_text = data["responseData"]["translatedText"]

            print("\nTranslated Hindi:")
            print(hindi_text)

            # Step 4: Generate Hindi voice
            async def generate_hindi_voice():
                communicate = edge_tts.Communicate(
                    hindi_text,
                    "hi-IN-SwaraNeural"
                )

                await communicate.save(str(output_file))

            asyncio.run(generate_hindi_voice())

            print("\nHindi voice created successfully!")
            print("Audio file:", output_file)

        else:
            print("Translation failed:", data.get("responseDetails"))

    except requests.RequestException as error:
        print("Network or translation error:", error)

    except Exception as error:
        print("An error occurred:", error)
