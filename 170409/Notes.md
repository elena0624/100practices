## 實際步驟
* 開始先套用之前用過的開啟小畫家範本python script，發現還未下載pyautogui  
  * 解決：
    * 至cmd pip install pyautogui，結果發現pyautogui是在anaconda裡面...
    * *~~疑問： 要如何在外面執行??(在未打開ANACONDA的情形下)(感覺是要把路徑移到外面)~~*
    其實放在桌面就可以了
 
* 程式撰寫部分
  * prtscreen的熱鍵名稱?
    * 不是 Ptr Sc，是printscreen(詳見參考資料)
  * python script如何中止？
    * 狂按ctrl+C
  * 中間間隔幾秒不能用moveTo，否則會失去滑鼠自由  
`import time`  
`time.sleep(2)`  
  
  * python for迴圈語法? 
  `for i in range(10, 0, -1):`

* 下一步
  * 撰寫自動連結wifi腳本
  * 新增介面輸入間隔秒數、持續時間、開始及停止按鈕

## 參考資料
* [Python控制鼠标和键盘-PyAutoGUI](http://blog.topspeedsnail.com/archives/5373)
