import pyautogui
import datetime
import time

screenSize = pyautogui.size()

def moveMouse():
    pyautogui.moveTo(5, screenSize[1], duration = 1)

def pressShift():
    for x in range(0,5):
        pyautogui.press('shift')

try:
    while True:
        hour = datetime.datetime.now().hour
        minutes = datetime.datetime.now().minute
        if (hour == 17 and minutes == 30) or hour == 12:
            print("end of day reached")
            quit()
        moveMouse()
        pressShift()
        time.sleep(10)
except KeyboardInterrupt:
    print("interupted")
    exit()
except pyautogui.FailSafeException:
    exit()
