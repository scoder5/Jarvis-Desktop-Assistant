import random
import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty("rate", 140)
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

user = ['hello', 'wake up', 'you there','howdy','hola','hey','hi','wassup','kaise ho','help','need']
bot = ['hello sir, welcome back','welcome back sir','at your service sir','how can i help you sir','hi sir']

def chatterbot(text):
    for word in text.split():
        if word in user:
            return random.choice(bot) + "."

response = chatterbot("hello")
