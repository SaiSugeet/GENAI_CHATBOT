import google.generativeai as genai
import pyttsx3
API_KEY = "Place Your API Key Here"   
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()
print("Test-Chatbot")
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)  
    engine.say(text)
    engine.runAndWait()
    engine.stop()  
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        farewell = "Goodbye"
        print("Chatbot:", bye)
        speak(bye)
        break
    response = chat.send_message(user_input)
    bot_reply = response.text
    print("Chatbot:", bot_reply)
    speak(bot_reply)
