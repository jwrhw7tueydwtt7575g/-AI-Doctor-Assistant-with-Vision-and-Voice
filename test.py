
import logging
from groq import Groq  # Assuming you're using the 'groq' library
import os

# Define the transcription function
def transcribe_with_groq(api_key, audio_path, model="whisper-large-v3"):
    try:
        # Initialize Groq client with API key
        client = Groq(api_key=api_key)

        # Open audio file and call the transcription API
        with open(audio_path, "rb") as f:
            logging.info("Transcribing with Groq Whisper...")

            # API call for transcription
            result = client.audio.transcriptions.create(
                model=model,
                file=f,
                language="en"
            )

            logging.info("Transcription complete.")
            return result.text  # Return the transcribed text

    except Exception as e:
        logging.error(f"Transcription error: {e}")
        return None

# Use your Groq API key and provide the audio file path
GROQ_API_KEY = "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"
AUDIO_FILE_PATH = "gtts_doctor.mp3"  # Replace with your audio file path

# Call the transcription function
transcription = transcribe_with_groq(GROQ_API_KEY, AUDIO_FILE_PATH)

if transcription:
    print(f"Transcription: {transcription}")
else:
    print("❌ Transcription failed.")











