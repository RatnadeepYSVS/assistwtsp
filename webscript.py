from datetime import datetime
from pynput.keyboard import Key,Controller
from pynput.mouse import Controller as Ctr,Button
import time,os
def whatssend(person,mess):
    os.system(r"C:\Users\ratna\Desktop\whatsapp.lnk")
    time.sleep(20)
    mouse=Ctr()
    keyboard=Controller()
    mouse.position=(200, 120)
    mouse.click(Button.left,1)
    for i in person:
        keyboard.press(i)
    time.sleep(8)
    keyboard.press(Key.down)
    time.sleep(2)
    mouse.position=(580,650)
    mouse.click(Button.left,1)
    time.sleep(2)
    while True:
        if datetime.now().hour==00 and datetime.now().minute==00:
            for i in mess:
                keyboard.press(i)
            time.sleep(2)
            keyboard.press(Key.enter)
            time.sleep(10)
            break
def normal_mes(person,msg):
    os.system(r"C:\Users\ratna\Desktop\whatsapp.lnk")
    time.sleep(20)
    mouse = Ctr()
    keyboard = Controller()
    mouse.position = (200, 120)
    mouse.click(Button.left, 1)
    for i in person:
        keyboard.press(i)
    time.sleep(8)
    keyboard.press(Key.down)
    time.sleep(2)
    mouse.position = (580, 650)
    mouse.click(Button.left, 1)
    time.sleep(2)
    for i in msg:
        keyboard.press(i)
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(10)