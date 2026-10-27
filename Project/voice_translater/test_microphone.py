
import sounddevice as sd

print("Checking available microphones...")

try:
    devices = sd.query_devices()

    print(devices)

    print("\nDefault microphone:")
    print(sd.query_devices(kind="input"))

except Exception as error:
    print("Microphone error:", error)
