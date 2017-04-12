# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:52:37 2017

@author: 毛荳荳
"""

import pyautogui
import time
time.sleep(5) #浪費3秒等他打開
pyautogui.press('win')
time.sleep(1) #浪費3秒等他打開
pyautogui.typewrite('chrome')#要先確定輸入法是英文
pyautogui.press('enter')
time.sleep(3) #浪費3秒等他打開c
pyautogui.hotkey('win','up')#最大化ㄍㄧㄠ
pyautogui.moveTo(1437,80,1)#選書籤
pyautogui.click()
pyautogui.moveTo(1336,140,1)#一道北大標籤
pyautogui.click()
pyautogui.moveTo(1242,425,3)#案登入
pyautogui.click()
time.sleep(3) #浪費3秒等他打開
pyautogui.press('win')
time.sleep(1) #浪費3秒等他打開
pyautogui.typewrite('pulse secure')
pyautogui.press('enter')
time.sleep(3) #浪費3秒等他打開
#pyautogui.screenshot('nctu.png')
#x,y = pyautogui.locateOnScreen('nctu.png')
#nctuButton = locateCenterOnScreen('nctu.png', grayscale=False)

#a,b,c,d = pyautogui.locateOnScreen(im)
a,b,c,d = pyautogui.locateOnScreen('nctu.png')
pyautogui.moveTo(a+250,b+20)
pyautogui.click()
time.sleep(3)#等待很重要!!!!!
pyautogui.typewrite('49222ef9')
pyautogui.press('enter')
