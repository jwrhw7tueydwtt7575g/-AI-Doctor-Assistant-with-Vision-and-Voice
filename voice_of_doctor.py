

# from gtts import gTTS
# import pygame
# import time

# def text_to_speech_with_gtts(input_text, output_filepath):
#     try:
#         tts = gTTS(text=input_text, lang='en', slow=False)
#         tts.save(output_filepath)

#         pygame.mixer.init()
#         pygame.mixer.music.load(output_filepath)
#         pygame.mixer.music.play()

#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)

#         return output_filepath
#     except Exception as e:
#         print(f"Error during TTS: {e}")
#         return None
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    try:
        # Generate speech
        tts = gTTS(text=input_text, lang='en', slow=False)
        tts.save(output_filepath)
        return output_filepath  # Just return path — Gradio will handle playback
    except Exception as e:
        print(f"Error during TTS: {e}")
        return None
