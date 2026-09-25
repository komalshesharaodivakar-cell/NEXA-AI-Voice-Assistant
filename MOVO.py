'''import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()
app.title("Movo")
app.geometry("400x700")

title = tk.Label(
    app,
    text="Calf Stretch",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)

# Load exercise image
image = Image.open("images/calf_stretch.png")
image = image.resize((300, 300))

photo = ImageTk.PhotoImage(image)

image_label = tk.Label(app, image=photo)
image_label.pack(pady=10)

instructions = tk.Label(
    app,
    text="How to do it:\n\n"
         "1. Stand facing a wall.\n"
         "2. Keep one leg behind you.\n"
         "3. Keep your back heel on the floor.\n"
         "4. Lean forward slowly.\n"
         "5. Hold for 20 seconds.",
    font=("Arial", 13),
    justify="left"
)

instructions.pack(pady=15)

start_button = tk.Button(
    app,
    text="Start 20 sec",
    font=("Arial", 16)
)

start_button.pack(pady=15)

app.mainloop()'''

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# -----------------------------
# Movo language content
# -----------------------------

translations = {
    "English": {
        "title": "Calf Stretch",
        "how": "How to do it:",
        "instructions": (
            "1. Stand facing a wall.\n"
            "2. Keep one leg behind you.\n"
            "3. Keep your back heel on the floor.\n"
            "4. Lean forward slowly.\n"
            "5. Hold for 20 seconds."
        ),
        "start": "Start 20 sec"
    },

    "Hindi": {
        "title": "पिंडली का स्ट्रेच",
        "how": "कैसे करें:",
        "instructions": (
            "1. दीवार के सामने खड़े हों।\n"
            "2. एक पैर पीछे रखें।\n"
            "3. पीछे की एड़ी जमीन पर रखें।\n"
            "4. धीरे-धीरे आगे झुकें।\n"
            "5. 20 सेकंड तक रोकें।"
        ),
        "start": "20 सेकंड शुरू करें"
    },

    "Kannada": {
        "title": "ಕಾಲಿನ ಹಿಂಭಾಗದ ಸ್ಟ್ರೆಚ್",
        "how": "ಹೇಗೆ ಮಾಡುವುದು:",
        "instructions": (
            "1. ಗೋಡೆಯ ಕಡೆಗೆ ಮುಖ ಮಾಡಿ ನಿಲ್ಲಿ.\n"
            "2. ಒಂದು ಕಾಲನ್ನು ಹಿಂದೆ ಇಡಿ.\n"
            "3. ಹಿಂದಿನ ಹಿಮ್ಮಡಿಯನ್ನು ನೆಲದ ಮೇಲೆ ಇಡಿ.\n"
            "4. ನಿಧಾನವಾಗಿ ಮುಂದೆ ಬಾಗಿ.\n"
            "5. 20 ಸೆಕೆಂಡುಗಳ ಕಾಲ ಹಿಡಿದುಕೊಳ್ಳಿ."
        ),
        "start": "20 ಸೆಕೆಂಡ್ ಪ್ರಾರಂಭಿಸಿ"
    },

    "Telugu": {
        "title": "కాల్ఫ్ స్ట్రెచ్",
        "how": "ఎలా చేయాలి:",
        "instructions": (
            "1. గోడకు ఎదురుగా నిలబడండి.\n"
            "2. ఒక కాలును వెనుకకు పెట్టండి.\n"
            "3. వెనుక మడమను నేలపై ఉంచండి.\n"
            "4. నెమ్మదిగా ముందుకు వంగండి.\n"
            "5. 20 సెకన్లు పట్టుకోండి."
        ),
        "start": "20 సెకన్లు ప్రారంభించండి"
    }
}


# -----------------------------
# Main window
# -----------------------------

app = tk.Tk()
app.title("Movo")
app.geometry("450x750")


# -----------------------------
# Image
# -----------------------------

image = Image.open("images/calf_stretch.png")
image = image.resize((300, 300))

photo = ImageTk.PhotoImage(image)


# -----------------------------
# Functions
# -----------------------------

def change_language(event=None):
    language = language_box.get()
    text = translations[language]

    title_label.config(text=text["title"])
    how_label.config(text=text["how"])
    instruction_label.config(text=text["instructions"])
    start_button.config(text=text["start"])


# -----------------------------
# Language selector
# -----------------------------

language_label = tk.Label(
    app,
    text="🌐 Language",
    font=("Arial", 14, "bold")
)

language_label.pack(pady=(15, 5))


language_box = ttk.Combobox(
    app,
    values=list(translations.keys()),
    state="readonly",
    font=("Arial", 13)
)

language_box.set("English")
language_box.pack(pady=5)

language_box.bind("<<ComboboxSelected>>", change_language)


# -----------------------------
# Exercise title
# -----------------------------

title_label = tk.Label(
    app,
    text="Calf Stretch",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=15)


# -----------------------------
# Exercise image
# -----------------------------

image_label = tk.Label(
    app,
    image=photo
)

image_label.pack(pady=10)


# -----------------------------
# Instructions
# -----------------------------

how_label = tk.Label(
    app,
    text="How to do it:",
    font=("Arial", 16, "bold")
)

how_label.pack(pady=(10, 5))


instruction_label = tk.Label(
    app,
    text=translations["English"]["instructions"],
    font=("Arial", 13),
    justify="left"
)

instruction_label.pack(pady=5)
# ------------------------------
# Language selection
# ------------------------------

language_label = tk.Label(
    app,
    text="🌐 Select Language",
    font=("Arial", 14)
)
language_label.pack(pady=5)
# ------------------------------
# Multilingual exercise instructions
# ------------------------------

instructions = {
    "English": """How to do it:
1. Stand facing a wall.
2. Keep one leg behind you.
3. Keep your back heel on the floor.
4. Lean forward slowly.
5. Hold for 20 seconds.""",

    "Hindi": """कैसे करें:
1. दीवार की ओर खड़े हों।
2. एक पैर पीछे रखें।
3. पीछे की एड़ी जमीन पर रखें।
4. धीरे-धीरे आगे झुकें।
5. 20 सेकंड तक रोकें।""",

    "Kannada": """ಮಾಡುವ ವಿಧಾನ:
1. ಗೋಡೆಯ ಕಡೆಗೆ ಮುಖ ಮಾಡಿ ನಿಲ್ಲಿ.
2. ಒಂದು ಕಾಲನ್ನು ಹಿಂದೆ ಇಡಿ.
3. ಹಿಂದಿನ ಹಿಮ್ಮಡಿಯನ್ನು ನೆಲದ ಮೇಲೆ ಇಡಿ.
4. ನಿಧಾನವಾಗಿ ಮುಂದೆ ಬಾಗಿ.
5. 20 ಸೆಕೆಂಡುಗಳ ಕಾಲ ಹಿಡಿದುಕೊಳ್ಳಿ.""",

    "Telugu": """ఎలా చేయాలి:
1. గోడకు ఎదురుగా నిలబడండి.
2. ఒక కాలును వెనుకకు పెట్టండి.
3. వెనుక మడమను నేలపై ఉంచండి.
4. నెమ్మదిగా ముందుకు వంగండి.
5. 20 సెకన్ల పాటు పట్టుకోండి.""",

    "Tamil": """எப்படி செய்வது:
1. சுவரை நோக்கி நிற்கவும்.
2. ஒரு காலை பின்னால் வைக்கவும்.
3. பின்புற குதிகாலை தரையில் வைக்கவும்.
4. மெதுவாக முன்னால் சாயவும்.
5. 20 விநாடிகள் வைத்திருக்கவும்.""",

    "Marathi": """कसे करावे:
1. भिंतीसमोर उभे रहा.
2. एक पाय मागे ठेवा.
3. मागची टाच जमिनीवर ठेवा.
4. हळूहळू पुढे झुका.
5. 20 सेकंद धरून ठेवा.""",

    "Bengali": """যেভাবে করবেন:
1. দেয়ালের দিকে মুখ করে দাঁড়ান।
2. একটি পা পিছনে রাখুন।
3. পিছনের গোড়ালি মাটিতে রাখুন।
4. ধীরে ধীরে সামনে ঝুঁকুন।
5. ২০ সেকেন্ড ধরে রাখুন।""",

    "Gujarati": """કેવી રીતે કરવું:
1. દિવાલ તરફ મોં કરીને ઊભા રહો.
2. એક પગ પાછળ રાખો.
3. પાછળની એડી જમીન પર રાખો.
4. ધીમે ધીમે આગળ ઝૂકો.
5. 20 સેકન્ડ સુધી રાખો.""",

    "Malayalam": """എങ്ങനെ ചെയ്യാം:
1. ചുവരിന് അഭിമുഖമായി നിൽക്കുക.
2. ഒരു കാൽ പിന്നിലേക്ക് വയ്ക്കുക.
3. പിന്നിലെ കുതികാൽ നിലത്ത് വയ്ക്കുക.
4. പതുക്കെ മുന്നോട്ട് വളയുക.
5. 20 സെക്കൻഡ് പിടിച്ചുനിൽക്കുക.""",

    "Punjabi": """ਕਿਵੇਂ ਕਰਨਾ ਹੈ:
1. ਕੰਧ ਵੱਲ ਮੂੰਹ ਕਰਕੇ ਖੜ੍ਹੇ ਹੋਵੋ।
2. ਇੱਕ ਪੈਰ ਪਿੱਛੇ ਰੱਖੋ।
3. ਪਿੱਛਲੀ ਅੱਡੀ ਜ਼ਮੀਨ 'ਤੇ ਰੱਖੋ।
4. ਹੌਲੀ-ਹੌਲੀ ਅੱਗੇ ਝੁਕੋ।
5. 20 ਸਕਿੰਟ ਲਈ ਰੋਕੋ।"""
}


def change_language(selected_language):
    instruction_label.config(
        text=instructions[selected_language]
    )

language_var = tk.StringVar(value="English")

language_menu = tk.OptionMenu(
    app,
    language_var,
    "English",
    "Hindi",
    "Kannada",
    "Telugu",
    "Tamil",
    "Marathi",
    "Bengali",
    "Gujarati",
    "Malayalam",
    "Punjabi",
    command=change_language
)

language_menu.config(font=("Arial", 12))
language_menu.pack(pady=5)
# ------------------------------
# 20 Second Exercise Timer
# ------------------------------

time_left = 20

def start_timer():
    global time_left

    if time_left > 0:
        timer_label.config(text=f"{time_left} sec")
        time_left -= 1
        app.after(1000, start_timer)
    else:
        timer_label.config(text="Exercise Complete! 🎉")
        time_left = 20

# -----------------------------
# Start button
# -----------------------------
timer_label = tk.Label(
    app,
    text="20 sec",
    font=("Arial",24,"bold")
)
timer_label.pack(pady=10)
start_button = tk.Button(
    app,
    text="Start 20 sec",
    font=("Arial", 16),
    padx=20,
    pady=10,
    command=start_timer
)

start_button.pack(pady=20)


# -----------------------------
# Start app
# -----------------------------

app.mainloop()