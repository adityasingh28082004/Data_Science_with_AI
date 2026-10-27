
import requests

url = "https://api.mymemory.translated.net/get"

params = {
    "q": "नमस्ते, आप कैसे हैं?",
    "langpair": "hi|ta"
}

try:
    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()

    if data.get("responseStatus") == 200:
        print("Tamil translation:")
        print(data["responseData"]["translatedText"])
    else:
        print("Translation service error:")
        print(data.get("responseDetails", "Unknown error"))

except requests.RequestException as error:
    print("Connection error:", error)

