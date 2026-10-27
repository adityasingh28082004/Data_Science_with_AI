
import os
import requests

api_key = os.getenv("BODHAN_API_KEY")

if not api_key:
    print("API key not found in this Command Prompt.")
else:
    url = "https://api.bodhan.ai/translate"

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "text": "Hello, how are you?",
            "target_language": "hi"
        },
        timeout=30
    )

    print("HTTP status:", response.status_code)
    print("Response:", response.text)
    print("Final URL:", response.url)
    print("Request ID:", response.headers.get("x-request-id"))
