import threading
import time

import win32gui

import myWindow


def stepEvent():
    myWindow1.moveLeft()
    win32gui.InvalidateRect(myWindow1.win, None, True)


def conti():
    while True:
        stepEvent()
        time.sleep(0.1)


myWindow1 = myWindow.MyWindow()

t1 = threading.Thread(target=conti)

t1.start()

myWindow1.mainStart()
