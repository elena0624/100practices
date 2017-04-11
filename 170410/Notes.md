## 實際步驟
* 讀取滑鼠位置，取得相關點擊位置
  * 利用下方代碼先取得各固定按鈕位置
```
#get position
while True:
    x,y = pyautogui.position()
    print(x,y)
```
* 查覺到很多動作都要等待時間，因此要適時加入
  * `time.sleep(2)#前面要記得import time`
* pyautogui.locateOnScreen的用法研究很久，最後發現要先
```
im = pyautogui.screenshot(region=(867,432, 80, 26))#先測好你要截圖的範圍
#有了上面這行im就會存到那個地方
#之後再用
x,y, a,b = pyautogui.locateOnScreen(im)
#x,y是圖片左上角，a,b是寬跟高
```

* 鍵入密碼
  * `pyautogui.typewrite('密碼')`

* 更多參考資料
  * [Doc PyAutoGUI](https://muxuezi.github.io/posts/doc-pyautogui.html)
  * [有關screenshot1](https://automatetheboringstuff.com/chapter18/)
  * [有關screenshot2](http://pyautogui.readthedocs.io/en/latest/screenshot.html)
  
* 再加入html等讀取就可以變成爬蟲了~ 下一步：存檔輸出、爬蟲....
