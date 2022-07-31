from pynput.keyboard import Key, Controller
import time
import os
import datetime


def hellochess(): 
    os.system("open -a TextEdit")
    time.sleep(2)
    keyboard = Controller()
    time.sleep(4)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press('L')
    keyboard.release('L')
    keyboard.press('G')
    keyboard.release('G')
    keyboard.press(' ')
    keyboard.release(' ')
    keyboard.press('C')
    keyboard.release('C')
    keyboard.press('H')
    keyboard.release('H')
    keyboard.press('E')
    keyboard.release('E')
    keyboard.press('S')
    keyboard.release('S')
    keyboard.press('S')
    keyboard.release('S')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    os.system("pkill Telegram")


day = datetime.timedelta(1)
starttime = time.time() 
totaltime = round((time.time() - starttime), 2)

while True:
    if totaltime % day.total_seconds() == 0:
        hellochess()
