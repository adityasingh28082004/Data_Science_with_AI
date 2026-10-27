
from faster_whisper import WhisperModel
from pathlib import Path
import requests
import asyncio
import edge_tts

# Find the audio file
audio_file = (
    Path(__file__).parent
    / "WhatsApp Audio 2026-10-25 at 7.11.26 AM.mp4"
)

# Check whether the audio file exists
if not audio_file.exists():
    print("Audio file not found:", audio_file)

else:
    # Load the speech recognition model
    print("Loading speech recognition model...")
    model = WhisperModel(
        "medium",
        device="cpu",
        compute_type="int8"
    )

    # Convert Hindi speech into text
    print("Recognizing Hindi speech...")

    segments, info = model.transcribe(
        str(audio_file),
        language="hi",
        vad_filter=True
    )

    # Collect recognized words into one sentence
    hindi_text = " ".join(
        segment.text.strip() for segment in segments
    ).strip()

    print("\nRecognized Hindi text:")
    print(hindi_text)

    # Translate Hindi into Tamil
    if hindi_text:
        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": hindi_text,
            "langpair": "hi|ta"
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
                tamil_text = data["responseData"]["translatedText"]

                print("\nTranslated Tamil text:")
                print(tamil_text)

                # Convert Tamil text into speech
                async def speak_tamil(text):
                    voice = "ta-IN-PallaviNeural"

                    communicate = edge_tts.Communicate(
                        text,
                        voice
                    )

                    output_file = (
                        Path(__file__).parent / "tamil_voice.mp3"
                    )

                    await communicate.save(str(output_file))

                    print("\nTamil audio created successfully!")
                    print("Audio file:", output_file)

                # Generate Tamil audio
                if tamil_text.strip():
                    try:
                        asyncio.run(speak_tamil(tamil_text))
                    except Exception as error:
                        print("Tamil audio generation failed:", error)

            else:
                print(
                    "Translation failed:",
                    data.get("responseDetails")
                )

        except requests.RequestException as error:
            print("Connection error:", error)

    else:
        print("No Hindi speech was recognized.")
