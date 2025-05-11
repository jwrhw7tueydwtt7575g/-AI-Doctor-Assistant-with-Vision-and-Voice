


import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import numpy as np
from noisereduce import reduce_noise
from scipy.io.wavfile import write
from groq import Groq

FFMPEG_PATH = r"C:\Users\mohan\Downloads\ffmpeg\ffmpeg.exe"
AudioSegment.converter = FFMPEG_PATH
logging.basicConfig(level=logging.INFO)

def record_audio(mp3_path, wav_path, timeout=20, phrase_time_limit=None):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Recording... Speak now!")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording finished.")

            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))

            samples = np.array(audio_segment.get_array_of_samples())
            if audio_segment.channels == 2:
                samples = samples.reshape((-1, 2))

            reduced = reduce_noise(y=samples, sr=audio_segment.frame_rate)

            write(wav_path, audio_segment.frame_rate, reduced.astype(np.int16))

            AudioSegment.from_wav(wav_path).export(mp3_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {mp3_path}")

    except Exception as e:
        logging.error(f"Error in recording: {e}")


def transcribe_with_groq(model, audio_path, api_key):
    try:
        client = Groq(api_key=api_key)
        with open(audio_path, "rb") as f:
            logging.info("Transcribing with Groq Whisper...")
            result = client.audio.transcriptions.create(
                model=model,
                file=f,
                language="en"
            )
            logging.info("Transcription complete.")
            return result.text
    except Exception as e:
        logging.error(f"Transcription error: {e}")
        return None
