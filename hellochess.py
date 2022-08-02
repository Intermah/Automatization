#pip3 install keyboard
import keyboard
import time
import os
from datetime import datetime
from datetime import timedelta

#Opens Telegram and prints message to the firt person on the list
def hellochess(): 
    os.system("open -a Telegram")
    #Time, required to open Telegram    
    time.sleep(4)
    keyboard.press_and_release('Down Arrow')
    keyboard.press_and_release('Enter')
    time.sleep(1)
    #Message, that you want to be printed
    keyboard.write("Man, LG play some chess")
    keyboard.press_and_release('Enter')

#This variable defines the period between sending messages (in seconds)
period = 15
curr = round(time.time())
#To change the period time unit to minutes, rewrite "seconds=period" to "minutes=period" 
exec_time = round(curr + timedelta(seconds=period).total_seconds())

#Wait, untill exec_time. than - our function writes a message 
while True:
    if curr != exec_time:
        time.sleep(1)
        curr = round(time.time())
    else:    
        hellochess()
        curr = round(time.time())
        #Updating the exec_time to make it run again
        exec_time = round(curr + timedelta(seconds=period).total_seconds())
    
