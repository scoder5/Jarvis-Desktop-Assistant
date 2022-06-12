import pyautogui as pt
from keyboard import press
from PIL import Image, ImageGrab
from time import sleep
import webbrowser as web

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image

def isCollide(data):
    for i in range(475, 590):
        for j in range(650, 700):
           if data[i,j] < 100:
               return True
    return False                  


def main():      
    web.open("https://chromedino.com/")
    print("Hacking the dinosaur game in 3 seconds...")
    sleep(5)
    pt.click(x=255, y=675)      
    pt.click(x=255, y=675)
    press('space')        

    while True:
        image = takeScreenshot()
        data = image.load()
        if isCollide(data):        
            press('space')                      

# image = takeScreenshot()
# data = image.load()         

# for i in range(425, 540):
#     for j in range(650, 700):
#         data[i,j] = 0
        
# image.show()

