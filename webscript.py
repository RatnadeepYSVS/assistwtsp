from datetime import datetime
from pynput.keyboard import Key,Controller
import time,webbrowser
def whatssend(date,month_num,person,mess):
    webbrowser.open('https://web.whatsapp.com/')
    time.sleep(20)
    keyboard=Controller()
    keyboard.press(Key.tab)
    time.sleep(3)
    for i in person:
        keyboard.press(i)
    time.sleep(8)
    keyboard.press(Key.tab)
    time.sleep(5)
    for i in range(2):
        keyboard.press(Key.tab)
    time.sleep(5)
    while True:
        if (datetime.now().day==date and datetime.now().month==month_num) and (datetime.now().hour==00 and datetime.now().minute==00):
            for i in mess:
                keyboard.press(i)
            time.sleep(5)
            keyboard.press(Key.enter)
            time.sleep(10)
            break
def normal_mes(person,msg):
    webbrowser.open('https://web.whatsapp.com/')
    time.sleep(20)
    keyboard=Controller()
    keyboard.press(Key.tab)
    time.sleep(3)
    for i in person:
        keyboard.press(i)
    time.sleep(5)
    keyboard.press(Key.tab)
    time.sleep(5)
    for i in range(2):
        keyboard.press(Key.tab)
    time.sleep(5)
    for i in msg:
        keyboard.press(i)
    time.sleep(5)
    keyboard.press(Key.enter)
