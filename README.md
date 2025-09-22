# GENAI_CHATBOT
This is a voice-enabled chatbot built using Google’s Gemini API (google-generativeai) and pyttsx3 for text-to-speech (TTS). You can chat with the bot in real-time and hear its responses.
🚀 Features

💬 Conversational AI powered by Gemini (gemini-2.0-flash).

🔊 Voice output using pyttsx3.

👋 Exit gracefully with commands like exit, quit, or bye.

⚡ Error handling for smoother experience.

🖥️ Simple terminal-based interface.

🛠️ Requirements

Python 3.8+

Packages:

pip install google-generativeai pyttsx3

🔑 Setup

Get an API Key from Google AI Studio
.

Replace the placeholder in API_KEY:

API_KEY = "Place Your API Key Here"

▶️ Usage

Run the chatbot with:

python chatbot.py


Example interaction:

Test-Chatbot
You: Hello
Chatbot: Hi there! How can I help you today?


To exit, type:

You: exit
Chatbot: Goodbye!

📂 Project Structure
📦 gemini-voice-chatbot
 ┣ 📜 chatbot.py      # Main chatbot script
 ┣ 📜 README.md       # Project documentation
 ┗ 📜 requirements.txt # Optional: dependencies

⚡ Future Improvements

🎙️ Add speech-to-text (STT) (e.g., speechrecognition or whisper) so you can talk to the bot instead of typing.

🎨 GUI-based chatbot using Tkinter or PyQt.

🌐 Deploy as a web app with Flask/FastAPI + WebSpeech API for browser voice chat.
