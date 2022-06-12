import os
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

while True:
    query = takeCommand().lower()

    if 'jarvis' in query:
        os.startfile("D:\\Python\\Jarvis\\jarvis.py")

    else:
        print(".......")
