# Google Gemini API Learning Repository

This repository contains Python scripts demonstrating various features of the Google Gemini API. It serves as a learning ground for understanding and experimenting with the API's capabilities.

## Examples

The following scripts showcase different aspects of the Gemini API:

*   `audio.py`: Demonstrates how to process audio files using the Gemini API. (Requires an audio file in `assets/`)
*   `document.py`: Shows how to analyze document content (e.g., PDFs) with the Gemini API. (Uses `assets/pdf/Founder-Mode.pdf`)
*   `images_descriptions.py`: Illustrates generating descriptions for multiple images stored in the `assets/` directory.
*   `list-file.py`: Example related to file listing or processing (further details might be needed based on the script's content).
*   `vison.py`: Demonstrates the vision capabilities of the Gemini API, likely analyzing images like `assets/a-cat.jpg`, `assets/bankak.jpg`, and `assets/quote.jpg`.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Alsadig-ahmed/gemini-API.git
    cd gemini-API
    ```
2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your Google Cloud credentials and Gemini API key.**
    *   You will need to obtain an API key from Google AI Studio or Google Cloud Console.
    *   The scripts typically expect the API key to be available as an environment variable named `GEMINI_API_KEY`. You can set it in your terminal like this:
        ```bash
        export GEMINI_API_KEY='YOUR_API_KEY'
        ```
        (On Windows Command Prompt, use `set GEMINI_API_KEY=YOUR_API_KEY`. On PowerShell, use `$env:GEMINI_API_KEY='YOUR_API_KEY'`)
    *   Refer to the official Google Cloud documentation for detailed authentication methods.

## Usage

Run the individual Python scripts to see the Gemini API in action:

```bash
python audio.py
python document.py
python images_descriptions.py
python list-file.py
python vison.py
```

Make sure you have the necessary asset files in the `assets/` directory as required by each script.
