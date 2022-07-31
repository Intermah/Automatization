#pip3 install keyboard
import keyboard
import time
import os
from datetime import datetime
from datetime import timedelta

def hellochess(): 
    os.system("open -a Telegram")
    time.sleep(4)
    keyboard.press_and_release('Down Arrow')
    keyboard.press_and_release('Enter')
    time.sleep(1)
    keyboard.write("Man, LG play some chess")
    keyboard.press_and_release('Enter')
    time.sleep(4)
    os.system("pkill Telegram")

#This variable defines the period through what messages will be sent
period = 1
curr = time.time()
const exec_time = curr + timedelta(minutes=period)

while True:
    if curr != exec_time:
        time.sleep(1)
        curr = time.time()
    else:    
        hellochess()
    
