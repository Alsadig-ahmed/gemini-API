import os
import base64
from google import genai
from google.genai import types
import mimetypes # To guess image mime types

# Load API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Configure the Gemini client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def image_to_base64(image_path):
    """Converts an image file to a base64 encoded string."""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def get_image_mime_type(image_path):
    """Guesses the MIME type of an image file."""
    mime_type, _ = mimetypes.guess_type(image_path)
    # Default to jpeg if type cannot be guessed, or handle specific cases
    if mime_type and mime_type.startswith('image/'):
        return mime_type
    # Add more specific checks if needed, e.g., based on file extension
    ext = os.path.splitext(image_path)[1].lower()
    if ext == '.jpg' or ext == '.jpeg':
        return 'image/jpeg'
    elif ext == '.png':
        return 'image/png'
    # Add other common image types if necessary
    return 'image/jpeg' # Fallback

def generate_description(image_path):
    """Generates a description for the image using Gemini API."""
    print(f"Processing image: {image_path}...")
    try:
        image_base64 = image_to_base64(image_path)
        mime_type = get_image_mime_type(image_path)
        image_part = types.Part.from_bytes(data=image_base64, mime_type=mime_type)
        prompt = "Describe this image in detail."
        response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    contents=[prompt, image_part])
        
        # Check if response has text content
        if response.text:
             # Accessing text safely, assuming the first part contains the text
             description = response.text
             print(f"Generated description for {os.path.basename(image_path)}")
             return description
        else:
             # Handle cases where the response might be blocked or empty
             print(f"Warning: No description generated for {os.path.basename(image_path)}. Response: {response}")
             # Check for safety ratings or other reasons for empty response
             if response.prompt_feedback.block_reason:
                 print(f"Generation blocked due to: {response.prompt_feedback.block_reason}")
             return None # Indicate failure or no description

    except Exception as e:
        print(f"Error generating description for {image_path}: {e}")
        return None

def process_images_in_folder(folder_path="assets"):
    """Processes all images in the specified folder."""
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found at {folder_path}")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file and looks like an image (basic check)
        if os.path.isfile(file_path) and get_image_mime_type(file_path).startswith('image/'):
            description = generate_description(file_path)
            
            if description:
                # Create the output text file path
                base_name = os.path.splitext(filename)[0]
                txt_filename = f"{base_name}.txt"
                txt_filepath = os.path.join(folder_path, txt_filename)
                
                try:
                    with open(txt_filepath, "w", encoding="utf-8") as txt_file:
                        txt_file.write(description)
                    print(f"Saved description to {txt_filepath}")
                except IOError as e:
                    print(f"Error writing description file {txt_filepath}: {e}")
        elif os.path.isfile(file_path):
             print(f"Skipping non-image file: {filename}")


if __name__ == "__main__":
    print("Starting image description generation...")
    process_images_in_folder()
    print("Image description generation complete.")
