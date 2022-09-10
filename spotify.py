import playsound
import pyautogui as pt
import keyboard
from time import sleep
import os
# import pyttsx3 as tts
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='en-in')
    filename = "voices.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def Spotify(name):
    speak("Playing it sir")
    os.startfile("C:\\Users\\surya\\AppData\\Roaming\\Spotify\\Spotify.exe")
    sleep(7)
    pt.click(x=82, y=123)
    sleep(1)
    pt.click(x=595, y=36)
    keyboard.write(name)
    sleep(4)
    pt.click(x=869, y=361)

