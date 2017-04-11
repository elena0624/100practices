# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 23:17:40 2017

@author: 毛荳荳
"""

import pyautogui
import time
#getsize
#print(pyautogui.size())
#1600x900

#getposition
while True:
    x,y = pyautogui.position()
    print(x,y)

#chrome位置:741,882
#書籤位置:1437,80
#北京大學網關:1242,425
#登陸按鈕1270,368
#time.sleep(5)
#im = pyautogui.screenshot(region=(900,230, 80, 26))
#print(im)
#pyautogui.screenshot('nctu.png')
x,y, a,b = pyautogui.locateOnScreen(im)
#print(x,y)