# 🧠 AI Doctor Assistant — Voice + Vision (Groq + LLaMA 4 + Whisper)

This project is a multimodal AI Doctor Assistant built using **Groq API**, **Whisper**, and **LLaMA 4**, combined into a clean and interactive **Gradio interface**. It lets users **speak symptoms**, **upload a medical image**, and get a **realistic doctor-style diagnosis**, including a **voice-based reply**.

---

## ✨ Features

- 🎙️ **Speech-to-Text** with `whisper-large-v3` (Groq)
- 🖼️ **Image + Text-based Diagnosis** with `LLaMA 4 Scout 17B` (Groq)
- 🔊 **Doctor's Response as Audio** using `gTTS` (Google Text-to-Speech)
- 🧠 Natural interaction that feels like talking to a real doctor
- 🧪 Useful for demos, education, early screening prototypes

---

## 🔧 Tech Stack

| Component              | Tool/Model Used                                  |
|------------------------|--------------------------------------------------|
| Voice Transcription    | Whisper Large v3 (Groq)                          |
| LLM for Diagnosis      | Meta LLaMA 4 Scout 17B (Groq)                    |
| Text-to-Speech         | gTTS (Google Text-to-Speech)                     |
| Audio Handling         | pydub, ffmpeg                                    |
| Web Interface          | Gradio                                           |
| API Key Management     | Python-dotenv                                    |

---

## 📸 Demo Screenshot

![WhatsApp Image 2025-05-11 at 23 24 37_965d076d](https://github.com/user-attachments/assets/56a31157-e428-4821-ae55-78c5c4d505b9)


---

## 📺 YouTube Walkthrough

🎥 **Watch the full video tutorial here:**  
👉 [Insert your YouTube Link]

Covers:
- Code walkthrough
- Setup instructions
- Live usage demo

---

## 🚀 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai-doctor-assistant
cd ai-doctor-assistant
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Install ffmpeg
Make sure ffmpeg is installed and added to PATH (needed for audio playback):

Download ffmpeg

4. Add .env file
Create a .env file with your Groq API Key:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
5. Run the App
bash
Copy
Edit
python gradio_app.py
Open your browser to http://127.0.0.1:7860

📁 Project Structure
vbnet
Copy
Edit
.
├── brain_of_doctor.py         # Handles Groq image+text query
├── voice_of_patient.py        # Handles audio transcription with Whisper
├── voice_of_doctor.py         # Text-to-speech + audio playback
├── gradio_app.py              # Gradio frontend + app logic
├── requirements.txt
├── .env                       # Your API key (not checked into Git)
└── README.md
🤖 System Prompt Design
The prompt was carefully crafted to:

Avoid AI-sounding responses

Encourage realistic, friendly medical tone

Keep responses under 2 sentences

No markdown, no technical preambles

📌 Limitations
Not intended for real medical use

Accuracy of diagnosis is illustrative only

Works best with clear images and speech

📬 Contact & Feedback
Want to collaborate or give feedback?
📩 [your.email@example.com]
🔗 LinkedIn: [linkedin.com/in/yourprofile]
🐦 Twitter: [@yourhandle]

