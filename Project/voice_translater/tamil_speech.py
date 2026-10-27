
from faster_whisper import WhisperModel
from pathlib import Path
import requests
import asyncio
import edge_tts

# Locate the Tamil audio file
audio_file = Path(__file__).parent / "sample_tamil.mp3"

if not audio_file.exists():
    print("Tamil audio file not found:", audio_file)

else:
    # Load the speech recognition model
    print("Loading speech recognition model...")

    model = WhisperModel(
        "medium",
        device="cpu",
        compute_type="int8"
    )

    # Convert Tamil speech into text
    print("Recognizing Tamil speech...")

    segments, info = model.transcribe(
        str(audio_file),
        language="ta",
        vad_filter=True
    )

    tamil_text = " ".join(
        segment.text.strip() for segment in segments
    ).strip()

    print("\nRecognized Tamil text:")
    print(tamil_text)

    if tamil_text:
        # Translate Tamil into Hindi
        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": tamil_text,
            "langpair": "ta|hi"
        }

        try:
            response = requests.get(
                url,
                params=params,
                timeout=20
            )
            response.raise_for_status()

            data = response.json()

            if data.get("responseStatus") == 200:
                hindi_text = data["responseData"]["translatedText"]

                print("\nTranslated Hindi text:")
                print(hindi_text)

                # Convert Hindi text into speech
                async def speak_hindi(text):
                    voice = "hi-IN-SwaraNeural"

                    communicate = edge_tts.Communicate(
                        text,
                        voice
                    )

                    output_file = (
                        Path(__file__).parent / "hindi_voice.mp3"
                    )

                    await communicate.save(str(output_file))

                    print("\nHindi audio created successfully!")
                    print("Audio file:", output_file)

                if hindi_text.strip():
                    try:
                        asyncio.run(speak_hindi(hindi_text))
                    except Exception as error:
                        print("Hindi audio generation failed:", error)

            else:
                print("Translation failed:", data.get("responseDetails"))

        except requests.RequestException as error:
            print("Connection error:", error)

    else:
        print("No Tamil speech was recognized.")
