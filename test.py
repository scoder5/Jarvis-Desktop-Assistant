import pyautogui as pt
from time import sleep

for i in range(3):
    sleep(2)
    pos = pt.position()
    print(pos)

a = input()
