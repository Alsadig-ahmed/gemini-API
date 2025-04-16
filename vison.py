from google import genai
import base64
from google.genai import types
import os 

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# image_base64 = image_to_base64("img/a-cat.jpg")
# prompt = "What is this image?"

image_base64 = image_to_base64("img/bankak.jpg")
prompt = "convert the image data to a json format"


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[prompt, types.Part.from_bytes(data=image_base64, mime_type="image/jpeg")])
   

print(response.text)
print('\n-------\n', response)
