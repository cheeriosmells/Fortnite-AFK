from tkinter import *
from threading import *
import pyautogui as pygui
import time
import sys
import random
from random import randint

root = Tk()

def StartFunction():
    pygui.FAILSAFE= False

class MouseFunctions(Thread):
    def run(self):
        # SpeedUntil_Location is in seconds.
                
        speedUntil_Location = 5
        movement1_X = 1684
        movement1_Y = 941

        movement2_X = 1746
        movement2_Y = 1050

        movement3_X = 803
        movement3_Y = 920

        movement4_X = 496
        movement4_Y = 953

        # Sleep Time
        sleepTime1 = 5
        sleepTime2 = 5
        sleepTime3 = 5
        sleepTime4 = 5
        # sleepTime1 = 55
        # sleepTime2 = 25
        # sleepTime3 = 25
        # sleepTime4 = 25

        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('Go')

        t_end = time.time() + 99999 * 99999
        while time.time() < t_end:
                        

                pygui.moveTo(movement1_X, movement1_Y, speedUntil_Location)
                pygui.click(clicks=1)
                time.sleep(sleepTime1)
                time.sleep(5)

                pygui.moveTo(movement2_X, movement2_Y, speedUntil_Location)
                pygui.click(clicks=1)
                time.sleep(sleepTime2)
                time.sleep(5)

                pygui.moveTo(movement3_X, movement3_Y, speedUntil_Location)
                pygui.click(clicks=1)
                time.sleep(sleepTime3)
                time.sleep(5)

                pygui.moveTo(movement4_X, movement4_Y, speedUntil_Location)
                pygui.click(clicks=1)
                time.sleep(sleepTime4)
                time.sleep(5)

class KeyboardFunctions(Thread):
    def run(self):
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('Go')

        while True:
            WASDmovement = ["w", "a", "s", "d"]
            

            randomMovement = random.choice(WASDmovement)

            if randomMovement=="w":
                print("w")
                pygui.keyDown('w')
                time.sleep(randint(1,20))
                pygui.keyUp('w')

            if randomMovement=="a":
                print("a")
                pygui.keyDown('a')
                time.sleep(randint(1,20))
                pygui.keyUp('a')

            if randomMovement=="s":
                print("s")
                pygui.keyDown('s')
                time.sleep(randint(1,20))
                pygui.keyUp('s')
                        
            if randomMovement=="d":
                print("d")
                pygui.keyDown('d')
                time.sleep(randint(1,20))
                pygui.keyUp('d')

        

t1 = MouseFunctions()
t2 = KeyboardFunctions()

t1.start()
t2.start()

def QuitFunction():
    exit()

button1 = Button(text="Quit", bg="white", fg="black", command=QuitFunction)
button2 = Button(text="Placeholder", bg="white", fg="black", command=StartFunction)

button1.pack(side=BOTTOM, fill=X)
button2.pack(side=TOP, fill=X)

root.wm_attributes("-topmost", 1)
root.geometry("208x52+0+0")
root.title("GUI")
root.resizable(width=False, height=False)
root.mainloop()
