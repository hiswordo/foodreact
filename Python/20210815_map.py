# chrome extension copy tab的格式 : # @link [[title]]([url]) at [date]
from functools import reduce

# ----高階函數---
# 就是把函數也當作參數傳遞進函數裡的函數
# ----映射函數（map）高級用法----
# ----map(function, sequence)----
# @link [【python入門教室】(11) 介紹內建高階函數- map, filter, reduce - iT 邦幫忙一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10230848) at 2021/8/15
# ! 對 sequence 中的 item 依次執行 function(item)，並將結果組成一個 「迭代器」
# @link [Python學習：映射函數（map）和函數式程式設計工具（filter和reduce） - 華為雲](https://www.huaweicloud.com/articles/de5393b2235a8ab61cb7ad587cac30f2.html) at 2021-08-14T16:13:15.
# 事實上，當list有規律的時候，用生成式，比較 pythonic。像是lst2 = [x*2 for x in lst]
# map最常見的基礎作用，對所有元素做動作，所以可以對str List轉int
# l = ['1','2','3','4']
# print(list(map(int,l)))

""" def sum3(x, y, z):
    return x + y + z #對於數字會加起來，對於字串會串接

list01 = [1, 2, 3, 4]
list02 = [1, 2, 3, 4]
list03 = [1, 2, 3, 4]

print(list(map(sum3, list01, list02, list03)))  # ! 這邊的sum不用sum()呼叫

list01 = ["2", "3", "10"]
list02 = ["1", "2", "3"]
list03 = ["5", "6", "7"]

print(list(map(sum3, list01, list02, list03))) """

# ----函數式程式設計工具（filter和reduce)----
# 由於range和filter都返回可反覆運算物件，在Python3.0中，它們需要list調用來顯示其所有結果。
# 返回值為 True 的項目組成一個 「迭代器」 返回
""" L = range(-10, 10)
print(list(filter(lambda x: x > 4, L)))
# print([x for x in range(-10, 10) if x > 4])  # 用等效生成式寫
# map，這個函數能夠用for 迴圈來等效，但是它是內置的，運行起來比較快。
# res = []
# for x in range(-10,10):
#     if x > 4:
#         res.append(x)
# print(res)

# iterator: function(function(item1, item2), item3)...以此類推
# 兩個兩個作用，也就是，lambda不能用三個引數來處理
print(reduce(lambda x, y: x + 2 * y, [1, 2, 3, 4, 5]))  # "+2y"的效果，持續加後面的
print(reduce(lambda x, y: x * y, [x for x in range(1, 6)]))  # 直接得到"5!" """

# l =[1,2,3,4]
# print(list(map(lambda x,y: x+y,l,l)))
# ??[2, 4, 6, 8]