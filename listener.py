import speech_recognition as sr
from config import LANGUAGE

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Ich höre...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=LANGUAGE)
        return text.lower()
    except:
        return ""