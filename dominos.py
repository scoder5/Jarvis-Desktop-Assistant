from time import sleep
from gtts import gTTS
import playsound
import webbrowser as web
import pyautogui as pt
import speech_recognition as sr
import os

def speak(text):
    tts = gTTS(text=text, lang='en-in')
    filename = "voicee.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def pizza():
    speak("Opening dominos sir")
    web.open("https://pizzaonline.dominos.co.in/menu?categoryId=2")
    sleep(2)
    speak("ordering it from your favourites sir")
    sleep(1)
    pt.mouseDown(x=-13, y=214)
    sleep(1)
    pt.moveTo(x=-14, y=256)
    pt.click(x=-14, y=256)
    sleep(2)

    for i in range(4):
        command = takeCommand().lower()

        if 'menu' in command:
            speak("I'll tell you the menu sir")

        elif 'cheese' in command:
            speak("ordering a cheese and corn sir")
            pt.click(x=-727, y=467)
            
        elif 'veg' in command:
            speak("Ordering a veg extravaganza sir")
            pt.click(x=-1557, y=468)














