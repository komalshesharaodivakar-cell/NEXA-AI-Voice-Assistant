import streamlit as st
from ollama import chat
import speech_recognition as sr
import pyttsx3
import yt_dlp
from datetime import datetime
import ctypes
import pyautogui
import requests


def get_weather(city="Bengaluru"):
    try:
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1},
            timeout=10
        ).json()

        if "results" not in geo:
            return "I couldn't find that location."

        location = geo["results"][0]

        weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": "temperature_2m,relative_humidity_2m,weather_code",
                "timezone": "auto"
            },
            timeout=10
        ).json()

        current = weather["current"]
        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]

        return f"It's currently {temperature}°C in {city}, with {humidity}% humidity."

    except Exception:
        return "Sorry Boss, I couldn't get the current weather."

def change_volume(action):
    if action == "up":
        ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0xAF, 0, 2, 0)

    elif action == "down":
        ctypes.windll.user32.keybd_event(0xAE, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0xAE, 0, 2, 0)

    elif action == "mute":
        ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0xAD, 0, 2, 0)

def find_song(song_name):
    try:
        options = {
            "quiet": True,
            "extract_flat": True,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            result = ydl.extract_info(
                f"ytsearch1:{song_name}",
                download=False
            )

        if result and result.get("entries"):
            return result["entries"][0].get("url")

            return None

    except Exception:
        return None

    except Exception as e:
        st.error(f"Music error: {e}")

    return None

# -----------------------------
# PAGE
# -----------------------------

st.set_page_config(
    page_title="Nexa",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Nexa")
st.subheader("That Thinks + Talks 🤖")

# -----------------------------
# 🧠 CONVERSATION MEMORY
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful Nexa. "
                "Give short, clear answers in 1-3 sentences. "
                "Remember the conversation and understand follow-up questions."
            )
        }
    ]

# -----------------------------
# 🔊 TEXT TO SPEECH
# -----------------------------
def play_music(command):
    command = command.lower().strip()

    if "increase volume" in command or "volume up" in command:
        change_volume("up")
        answer = "Volume increased."
        st.success(f"🔊 {answer}")
        speak(answer)

    elif "decrease volume" in command or "volume down" in command:
        change_volume("down")
        answer = "Volume decreased."
        st.success(f"🔉 {answer}")
        speak(answer)

    elif "mute" in command:
        change_volume("mute")
        answer = "Muted."
        st.success(f"🔇 {answer}")
        speak(answer)

    if "relaxing" in command:
        search = "relaxing Hindi songs"
    elif "trending" in command:
        search = "trending Hindi songs India"
    elif "chatpate" in command:
        search = "latest energetic Hindi songs"
    elif command.startswith("play "):
        search = command[5:]
    else:
        return None

    try:
        options = {
            "quiet": True,
            "extract_flat": True,
            "skip_download": True
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            result = ydl.extract_info(
                f"ytsearch1:{search}",
                download=False
            )

        if result and result.get("entries"):
            return result["entries"][0]["webpage_url"]

    except Exception:
        return None

    return None

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# -----------------------------
# 🤖 AI FUNCTION
# -----------------------------

def ask_ai(question):

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    response = chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]
    return answer

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    return answer

# -----------------------------
# ⌨️ TEXT INPUT
# -----------------------------

st.divider()
st.subheader("⌨️ Type Your Question")

user_input = st.text_input(
    "Type here:",
    placeholder="Ask me anything..."
)

if st.button("Send 🚀"):

    if user_input.strip():

        command = user_input.lower().strip()

        if command.startswith("play "):
            song_name = command[5:].strip()

            if song_name:
                st.info(f"🔎 Finding {song_name}...")
                music_url = find_song(song_name)

                if music_url:
                    st.success(f"🎵 Playing {song_name}")

                    st.components.v1.html(
                        f"""
                        <iframe
                            width="100%"
                            height="400"
                            src="{music_url.replace('watch?v=', 'embed/')}?autoplay=1"
                            frameborder="0"
                            allow="autoplay; encrypted-media"
                            allowfullscreen>
                        </iframe>
                        """,
                        height=420
                    )

                    answer = f"🎵 Playing {song_name}"
                else:
                    answer = "❌ I couldn't find that song."
            else:
                answer = "🎵 Tell me which song to play."

        else:
            with st.spinner("🤖 Thinking..."):
                answer = ask_ai(user_input)
                st.success("🤖 AI Response")
                st.write(answer)
                speak(answer)
    else:
        st.warning("Please type something.")

# -----------------------------
# 🎤 VOICE INPUT
# -----------------------------

st.divider()
st.subheader("🎤 Nexa")

if st.button("🎤 Start Speaking"):

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            st.info("🎤 Listening... Speak now!")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            recognizer.pause_threshold = 0.8
            recognizer.non_speaking_duration = 0.5
            recognizer.phrase_threshold = 0.3

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        st.info("🧠 Understanding...")

        voice_text = recognizer.recognize_google(audio)
        # 🎵 Play any song from voice command
        command = voice_text.lower().strip()

        # 🔊 Volume control
        if "increase volume" in command or "volume up" in command:
            pyautogui.press("volumeup",presses=10, interval=0.05)
            answer = "🔊 Volume increased"
            st.write(answer)
            speak(answer)

        elif "decrease volume" in command or "volume down" in command:
            pyautogui.press("volumedown", presses=10, interval=0.05)
            answer = "🔉 Volume decreased"
            st.write(answer)
            speak(answer)

        elif "mute" in command:
            pyautogui.press("volumemute")
            answer = "volume muted"
            st.write(answer)
            speak(answer)

        elif "unmute" in command:
            pyautogui.press("volumemute")
            answer = "volume unmuted"
            st.write(answer)
            speak(answer)

        if "what time" in command or "time is it" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            answer = f"The current time is {current_time}."
            st.success(f"⏰ {answer}")
            speak(answer)

        if "what is today's date" in command or "what's today's date" in command:
            current_date = datetime.now().strftime("%d %B %Y")
            answer = f"Today's date is {current_date}."
            st.success(f"📅 {answer}")
            speak(answer)

        if "good morning" in command:
            answer = "Good morning! I'm NEXA. How can I help you?"
            st.success(f"🌅 {answer}")
            speak(answer)

        if "good night" in command:
            answer = "Good night! Sleep well. I'll be here when you need me."
            st.success(f"🌙 {answer}")
            speak(answer)

        elif command.startswith("play "):
            song_name = command[5:].strip()

            if song_name:
                st.info(f"🔎 Finding {song_name}...")
                music_url = find_song(song_name)

                if music_url:
                    st.success(f"🎵 Playing {song_name}")
                    st.components.v1.html(
                        f"""
                        <iframe
                            width="100%"
                            height="400"
                            src="{music_url.replace('watch?v=', 'embed/')}?autoplay=1"
                            frameborder="0"
                            allow="autoplay; encrypted-media"
                            allowfullscreen>
                        </iframe>
                        """,
                        height=420
                    )
                else:
                    st.error("❌ I couldn't find that song.")

        st.success("🗣️ You said:")
        st.write(voice_text)

        if command.startswith("play "):
            answer = f"🎵 Playing {song_name}"

        elif not any(x in command for x in
                     ["increase volume", "decrease volume", "volume up", "volume down", "mute", "unmute","what time", "time is it", "what is today's date", "what's today's date", "good morning","good night"]):
            with st.spinner("🤖 Thinking..."):
                answer = ask_ai(voice_text)

        st.success("🤖 AI Response")
        st.write(answer)

        speak(answer)

    except sr.WaitTimeoutError:
        st.warning("⏱️ I didn't hear you.")

    except sr.UnknownValueError:
        st.warning("😅 I couldn't understand you.")

    except sr.RequestError:
        st.error("🌐 Speech recognition needs internet.")

    except Exception as e:
        st.error(f"❌ Error: {e}")

# -----------------------------
# 🧠 MEMORY STATUS
# -----------------------------

st.divider()

st.caption(
    f"🧠 Conversation memory: "
    f"{len(st.session_state.messages) - 1} messages"
)

if st.button("🗑️ Clear Conversation"):
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI voice assistant. "
                "Give short, clear answers in 1-3 sentences. "
                "Remember the conversation and understand follow-up questions."
            )
        }
    ]
    st.rerun()

# -----------------------------
# 🎵 MUSIC PLAYER
# -----------------------------

st.divider()
st.subheader("🎵 Music Player")

music_choice = st.selectbox(
    "Choose music:",
    [
        "Relaxing Music",
        "Study / Focus Music",
        "Peaceful Music"
    ]
)

music_links = {
    "Relaxing Music":
        "https://www.youtube.com/watch?v=qycqF1CWcXg",

    "Study / Focus Music":
        "https://www.youtube.com/watch?v=qycqF1CWcXg",

    "Peaceful Music":
        "https://www.youtube.com/watch?v=CcsUYu0PVxY"
}

if st.button("▶️ Play Music"):
    st.video(music_links[music_choice])

# -----------------------------
# 🎵 MUSIC ZONE
# -----------------------------

st.divider()
st.subheader("🎵 Music Zone")

music_category = st.selectbox(
    "Choose your mood:",
    [
        "😌 Relaxing",
        "🔥 Trending",
        "🌶️ Chatpate"
    ]
)

music_links = {
    "😌 Relaxing": "https://www.youtube.com/watch?v=gkSO4JmJ8L4",
    "🔥 Trending": "https://www.youtube.com/watch?v=zAiIgYOH4Ys",
    "🌶️ Chatpate": "https://www.youtube.com/watch?v=cWMxCE2HTag"
}
# 🎤 Voice command → Music
if "voice_text" in locals():
    command = voice_text.lower()

    if "relax" in command:
        music_choice = "Relaxing"
    elif "study" in command or "focus" in command:
        music_choice = "Study / Focus Music"
    elif "peaceful" in command or "peace" in command:
        music_choice = "Peaceful"

    if "music" in command:
        st.success(f"🎵 Playing {music_choice}")
        st.video(music_links[music_choice])

if st.button("▶️ Play Music", key="music_play_buttton"):
    st.video(music_links[music_category])

