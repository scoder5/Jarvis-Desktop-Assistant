import random
import playsound
from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en-in')
    filename = "voic.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

user = ['hello', 'wake up', 'you there','howdy','hola','hey','hi','wassup','kaise ho','help','need']
bot = ['hello sir, welcome back','welcome back sir','at your service sir','how can i help you sir','hi sir']

def chatterbot(text):
    for word in text.split():
        if word in user:
            return random.choice(bot) + "."

response = chatterbot("hello")