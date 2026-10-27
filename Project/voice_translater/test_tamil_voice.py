

import asyncio
import edge_tts
from pathlib import Path

async def main():
    tamil_text = "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?"

    voice = "ta-IN-PallaviNeural"

    output_file = Path(__file__).parent / "sample_tamil.mp3"

    communicate = edge_tts.Communicate(tamil_text, voice)

    await communicate.save(str(output_file))

    print("Tamil audio created successfully!")
    print("File location:", output_file)

asyncio.run(main())
