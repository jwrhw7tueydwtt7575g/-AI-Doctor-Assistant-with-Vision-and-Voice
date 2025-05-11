import os
import gradio as gr
from brain_of_doctor import encode_image, analyze_image_with_query
from voice_of_patient import transcribe_with_groq
from voice_of_doctor import text_to_speech_with_gtts
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# System prompt for the doctor assistant
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Donot say 'In the image I see' but say 'With what I see, I think you have ....'
Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""

# Processing function
def process_inputs(audio_filepath, image_filepath):
    transcription = transcribe_with_groq(
        model="whisper-large-v3",
        audio_path=audio_filepath,
        api_key=GROQ_API_KEY
    )

    if not transcription:
        return "Failed to transcribe", "No response", None

    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + transcription,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    output_voice_path = text_to_speech_with_gtts(doctor_response, "doctor_response.mp3")

    return transcription, doctor_response, output_voice_path

# Gradio interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Your Voice"),
        gr.Image(type="filepath", label="Upload Face Image")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice Response")
    ],
    title="🧠 AI Doctor Assistant with Vision and Voice"
)

# Launch the app
iface.launch(debug=True)

