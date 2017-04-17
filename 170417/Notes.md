**把以前的資料庫先拿出來用用看**
## 重新安裝XAMPP(有無自動更新or更新程式?)
* 先備份htdocs
    * 忘記備份資料庫了...........................................................
    * 所以只剩網頁框架在，資料庫內容要重建
* 無法啟動apache，原因：與VMware Station衝突(http://kaikai.info/xampp-vmware-conflict/)
    * 把VMware遠程存取的地方disabled掉，反正用不到
* 跳出警告：
> Deprecated: mysql_connect(): The mysql extension is deprecated and will be removed in the future: use mysqli or PDO instead  
    * PDO => php5以上擁有 到底怎麼用

## 
