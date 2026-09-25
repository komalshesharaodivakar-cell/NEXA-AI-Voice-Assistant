import pyttsx3
import speech_recognition as sr
import ollama
import subprocess

# -----------------------------
# 🔊 Text-to-Speech
# -----------------------------
engine = pyttsx3.init()

engine.say("Hello! I am Nexa.")
engine.runAndWait()


# -----------------------------
# 🎤 Speech Recognition
# -----------------------------
recognizer = sr.Recognizer()


# -----------------------------
# 🔧 Query Processing
# -----------------------------
def process_query(text):
    text = text.strip()
    text = " ".join(text.split())
    return text

# -----------------------------
# 🧠 Query Type Detection
# -----------------------------
def detect_query_type(text):
    command_words = ["open", "launch", "start", "close"]

    words = text.lower().split()

    if words and words[0] in command_words:
        return "COMMAND"

    if text.lower().startswith(
        ("what", "why", "how", "when", "where", "who", "can", "is", "are")
    ):
        return "QUESTION"

    return "CONVERSATION"


# -----------------------------
# 🧠 Conversation Memory
# -----------------------------
conversation_history = [
    {
        "role": "system",
        "content": (
            "You are a friendly personal AI voice assistant. "
            "You are helpful, calm, natural, and conversational. "
            "You are speaking directly to the user through a microphone and speaker. "
            "Keep your answers concise and easy to understand when spoken aloud. "
            "Do not use unnecessary markdown, long lists, or complicated formatting. "
            "Remember the conversation during the current session and use previous messages when relevant."
        )
    }
]



print("\n🤖 Assistant is ready!")
print("Say something, or say 'exit' to stop.\n")


# -----------------------------
# 🔄 Continuous Conversation
# -----------------------------
while True:

    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    print("🧠 Processing...")

    try:
        text = recognizer.recognize_google(audio)

        # 🔧 Process the recognized query
        text = process_query(text)

        query_type = detect_query_type(text)

        print("You said:", text)
        print("📌 Query Type:", query_type)

        if query_type == "COMMAND":
            print("💻 Processing computer command...")

        elif query_type == "QUESTION":
            print("🧠 Sending question to AI...")
            
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand you.")
        continue

    except sr.RequestError:
        print("❌ Speech recognition service is unavailable.")
        continue
    if text.lower() in ["exit", "quit", "stop", "goodbye"]:
            print("👋 Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break
    # -----------------------------
    # 💻 Computer Commands
    # -----------------------------
    command = text.lower()

    if "open chrome" in command:
        print("🌐 Opening Chrome...")
        engine.say("Opening Chrome.")
        engine.runAndWait()
        subprocess.Popen("start chrome", shell=True)
        continue
    elif "open calculator" in command:
        print("🧮 Opening Calculator...")
        engine.say("Opening Calculator.")
        engine.runAndWait()
        subprocess.Popen("calc.exe")
        continue
    elif "open notepad" in command:
        print("📝 Opening Notepad...")
        engine.say("Opening Notepad.")
        engine.runAndWait()
        subprocess.Popen("notepad.exe")
        continue
    elif "open file explorer" in command:
        print("📁 Opening File Explorer...")
        engine.say("Opening File Explorer.")
        engine.runAndWait()
        subprocess.Popen("explorer.exe")
        continue
    elif "open youtube" in command:
        print("▶️ Opening YouTube...")
        engine.say("Opening YouTube.")
        engine.runAndWait()
        subprocess.Popen(
            'start "" "https://www.youtube.com"',
            shell=True
        )
        continue
    elif "open google" in command:
        print("🔎 Opening Google...")
        engine.say("Opening Google.")
        engine.runAndWait()
        subprocess.Popen(
            'start "" "https://www.google.com"',
            shell=True
        )
        continue
    elif "open github" in command:
        print("🐙 Opening GitHub...")
        engine.say("Opening GitHub.")
        engine.runAndWait()
        subprocess.Popen(
            'start "" "https://github.com"',
            shell=True
        )
        continue


    # -----------------------------
    # 🛑 Exit command
    # -----------------------------
    if text.lower() in ["exit", "quit", "stop", "goodbye"]:
        print("👋 Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        break


    # -----------------------------
    # ➕ Add user's message
    # -----------------------------
    conversation_history.append(
        {
            "role": "user",
            "content": text
        }
    )


    # -----------------------------
    # 🧠 Ask Ollama
    # -----------------------------
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=conversation_history
        )

        ai_response = response["message"]["content"]

        print("🤖 AI:", ai_response)


        # -----------------------------
        # ➕ Remember AI response
        # -----------------------------
        conversation_history.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )


        # -----------------------------
        # 🔊 Speak response
        # -----------------------------
        engine.say(ai_response)
        engine.runAndWait()


    except Exception as e:
        print("❌ Ollama error:", e)