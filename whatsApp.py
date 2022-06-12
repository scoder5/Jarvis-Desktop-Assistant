from os import startfile
from pyautogui import click
from keyboard import press, write
from time import sleep

def whatsAppCall(name):
    startfile("C:\\Users\\surya\\OneDrive\\Desktop\\WhatsApp.lnk")
    sleep(16)
    click(x=277, y=135)
    write(name)
    sleep(3)
    press('enter')
    click(x=1722, y=62)

def whatsAppVideocall(name):
    startfile("C:\\Users\\surya\\OneDrive\\Desktop\\WhatsApp.lnk")
    sleep(16)
    click(x=277, y=135)
    write(name)
    sleep(3)
    press('enter')
    click(x=1660, y=59)
