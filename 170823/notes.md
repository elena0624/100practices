# list 可自由變動
* append 在後面插元素 ex.lst.append([7,8]) 會直接加一個list進去
* list.count 計算在list裡面出現了幾次 ex.lst.count('yo')
* extend 在後面加元素ex.lst.extend([7,8]) 
* insert 會把元素往後推 ex.lst.insert(1,9) 在哪個位置插哪個(第一個是0)
* remove 直接把它刪掉 ex.lst.remove(9) 這樣會刪掉第一個
* pop 把那個位置的元素丟出來 ex.lst.pop(2)
* index 找出那個元素的index值 ex.lst.index(1)
* sort 排序 ex.lst(reverse=True) 反著排
* copy
* clear 
* del ex.del lst[2:3]
# dequeue
# tuple
* 宣告tuple直接逗點就好 ex. t=1,2,3
* tuple[0] 就會=1
* 可是不能用tuple[0]=3 因為tuple裡面的值不能修改跟刪除
* list of list裡面存的是指標 因此不能直接改值可是可以改t[2][0]=3
help(list.pop)

# dictionary
* dic={'bb':23,'yy':34}
* dic['bb']會=23
# string 
* stri = "3331234567"
* stri.split('2') 把string裡面想隔開的東西由2切成list
# sets
* 沒有順序沒有重複的元素 可用set()建立


# numpy
* np.random.randint
* np.sort() 

# pandas
* 用在數據處理
* series -一維的 ex.pd.Series(data, index=index) / pd.Series([1,2,3,3], index=['a','b','c','d'])
* dataframe -二維的 ex.
  * xy 軸都可以自己設label
  * ex. pandas.DataFrame(data=None, index=None, columns=None, dtype=None)
