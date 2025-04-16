from google import genai
import base64
from google.genai import types
import os 

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

with open('assets/audio.opus', 'rb') as f:
    audio_bytes = f.read()


response = client.models.generate_content(
    model="gemini-2.0-flash",
    # contents=["What is this image?",
    contents=["generate a transcription for this audio",
    types.Part.from_bytes(data=audio_bytes, mime_type="audio/opus")])
   

print(response.text)
print('\n-------\n', response)






