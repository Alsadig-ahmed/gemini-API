# Gemini API and Facebook Graph API Examples

This project demonstrates the use of the Google Gemini API for image analysis and audio transcription.

## Features

- **Image Analysis (`vison.py`):** Uses the Gemini API (`gemini-2.0-flash`) to analyze images. The current example extracts data from an image and formats it as JSON.
- **Audio Transcription (`audio.py`):** Uses the Gemini API (`gemini-2.0-flash`) to transcribe audio files. The current example transcribes an `.opus` audio file.

## Setup

1.  **Clone the repository :**

    ```bash
    git clone https://github.com/Alsadig-ahmed/gemini-API.git
    cd gemini-API
    ```

2.  **Install dependencies:**
    Make sure you have Python installed. Then, install the required packages using pip:

    ```bash
    python -m venv myenv && source myenv/bin/activate

    pip install -r requirements.txt
    ```

3.  **Configure Google Gemini API Key:**
    The scripts `vison.py` and `audio.py` require a Google Gemini API key. Set it as an environment variable:

    ```bash
    export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

    Replace `"YOUR_GEMINI_API_KEY"` with your actual key. You might want to add this line to your shell configuration file (e.g., `.bashrc`, `.zshrc`) for persistence.

## Usage

Run the scripts individually using Python:

- **Image Analysis:**

  ```bash
  python vison.py
  ```

  _(Modify the `image_path` and `prompt` variables inside `vison.py` to analyze different images or perform different tasks.)_

- **Audio Transcription:**

  ```bash
  python audio.py
  ```

  _(Modify the audio file path inside `audio.py` to transcribe different audio files.)_

## Dependencies

All required Python packages are listed in the `requirements.txt` file.
