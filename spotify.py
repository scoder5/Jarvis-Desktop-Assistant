import pyautogui as pt
import keyboard
from time import sleep
import os
import pyttsx3 as tts

def speak(text):
    engine = tts.init('sapi5')
    engine.say(text)
    engine.runAndWait()

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

