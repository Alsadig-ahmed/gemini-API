from google import genai
import base64
from google.genai import types
import pathlib
import os 

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

file_path = pathlib.Path('assets/pdf') / 'Founder-Mode.pdf'
file_path.read_bytes()

# Upload the PDF using the File API
sample_doc = client.files.upload(file=file_path)
# sample_doc = client.files.get(name="files/i9q7pkzdc6e7")

prompt="Summarize this document"

response = client.models.generate_content(
  model="gemini-2.0-flash",
  contents=[sample_doc, prompt])
  
res = response.text  
print(res)
# file_path = pathlib.Path('assets/pdf') / 'Founder-Mode.txt'
# file_path.write_bytes(res.encode("utf-8"))

