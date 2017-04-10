import pyautogui
import time
pyautogui.FAILSAFE = False
for i in range(0, 10, 1):
    #pyautogui.moveTo(0,0,2)
    time.sleep(2)
    pyautogui.hotkey('win','printscreen')
