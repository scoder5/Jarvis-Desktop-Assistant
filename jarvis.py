import pyttsx3
#import playsound
import speech_recognition as sr
import webbrowser as web
import keyboard
from time import sleep
import os
import dominos
from whatsApp import *
import chatBot
import random
import dino
import spotify
import pyautogui as pt

engine = pyttsx3.init()
voices = engine.getProperty('voices')   
engine.setProperty("rate", 120)
engine.setProperty('voice', voices[1].id)

user = ['hello', 'wake up', 'you there','howdy','hola','hey','hi','wassup','kaise ho','help','need']
bot = ['hello sir, welcome back','welcome back sir','at your service sir','how can i help you sir','hi sir']

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chatterbot(text):
    for word in text.split():
        if word in user:
            return random.choice(bot) + "."

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
  
speak("Welcome back sir")
##response = chatterbot("hello")
##speak(response)

while True:
    query = takeCommand().lower()

    if 'hello' in query:
        speak("hello sir")

    elif 'open google' in query:
        speak("Opening google sir")
        web.open("https://www.google.co.in/")

    elif 'play music' in query:
        speak("playing it sir")
        os.startfile("C:\\Users\\surya\\AppData\\Roaming\\Spotify\\Spotify.exe")
        sleep(4)
        keyboard.press('space')

    elif 'open youtube' in query:
        speak("Opening youtube")
        web.open("https://www.youtube.com/")

    elif 'classroom' in query:
        speak("do we have a test today sir")
        web.open("https://classroom.google.com/h")

    elif 'pizza' in query:
        dominos.pizza()

    elif 'call' in query:
       speak("placing the call sir")
       name = query.replace("call ", "")
       Name = query.replace("jarvis ", "")
       Name = str(name)
       whatsAppCall(Name)

    elif 'dinosaur' in query:
        speak("Hacking it for you sir..")
        dino.main()

    elif 'break' in query:
        speak("you can call me anytime sir")
        quit()

    elif 'play' in query:
        name = query.replace("play ", "")
        Name = query.replace("jarvis ", "")
        Name = str(name)
        spotify.Spotify(Name)

    elif 'increase' in query:
        pt.press("volumeup")

    elif 'decrease' in query:
        pt.press("volumedown")

    elif 'mute' in query:
        pt.press("volumemute")

    elif 'WhatsApp' in query:
        speak("Opening whatsApp web")
        web.open("https://web.whatsapp.com/")
        
    elif 'shutdown' in query:
        speak("shutting down the system, bye sir!")
        os.system("shutdown /s /t 1")

    elif 'panel' in query:
        keyboard.press("windows + a")
        
    elif 'cmd' in query:
        keyboard.press_and_release('windows + r')
        sleep(0.5)
        keyboard.write('cmd')
        keyboard.press("enter")

        
        
        
        
        





    

    
