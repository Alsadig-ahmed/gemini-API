from google import genai
import os 

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# list using the File API
for file in client.files.list():
    print(file.name)

# delete a file 
response = client.files.delete(name="files/7mlwugy8icld")

# file = client.files.get(name=file.name)
# print(file)