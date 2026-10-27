
import sounddevice as sd
import soundfile as sf
from pathlib import Path

# Recording settings
duration = 5
sample_rate = 16000
output_file = Path(__file__).parent / "microphone_test.wav"

print("Speak in Hindi or Tamil for 5 seconds...")
print("Recording started!")

try:
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
        device=5
    )

    sd.wait()

    sf.write(str(output_file), audio, sample_rate)

    print("\nRecording completed successfully!")
    print("Saved file:", output_file)

except Exception as error:
    print("\nRecording failed:", error)
