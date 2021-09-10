# ---- zip ----
# @link [Python 列表乘法：如何在 Python 中將列表相乘 - 0x資訊](https://0xzx.com/zh-tw/2021062223531537358.html) at 2021/9/5
# @link [Python 使用 zip 與 for 迴圈同時對多個 List 進行迭代 - G. T. Wang](https://blog.gtwang.org/programming/python-iterate-through-multiple-lists-in-parallel/) at 2021/9/7
# zip(A, B) 會將 A 與 B 的每個元素以一對一的方式配對起來，組成一個新的迭代器

# ---< 配對相乘 >---
# 相當於numpy的乘法
listA = [1, 2, 3]
listB = [4, 5, 6]
products = []

for dt1, dt2 in zip(listA, listB):
    products.append(dt1 * dt2)

print(products)

# *生成式寫法
products = [x * y for x, y in zip(listA, listB)]
print(products)

# @link [python - 将数组元素的所有组合相乘 - IT工具网](https://www.coder.work/article/2438976) at 2021/9/5
import numpy as np

t = [3, 4]
b = [1, 2, 3, 4]
print(f'{np.outer(t, b) = }')
# array([[ 3,  6,  9, 12],
#        [ 4,  8, 12, 16]])

# ---< 配對出tuple list or dict >---
items1 = zip(["a", "b", "c"], ["12", "34", "56"])
items2 = dict(zip(["a", "b", "c"], "123"))  # {'a': '1', 'b': '2', 'c': '3'}
# zip回傳迭代器物件 <zip object at 0x000000000263C100>，在python 2是則是tuple list
print(f'{items1 = }') 
print(f'{list(items1) = }')
print(f'{items2 = }')

# ---< 性質 >---
# 長度不足，則以短的為限
names2 = ["A", "B", "C"]
values2 = [11, 23]
for x, y in zip(names2, values2):
    print(x, y)

# 利用itertools 以長度最長的 List 為準，不夠則補"None"
from itertools import zip_longest
for x,y in zip_longest(names2, values2):
    print(x, y)

# ---< Unzip from tuple list or dict >---
# 打包成 Tuples 組成的 List
names = ["A", "B", "C"]
values = [11, 23, 70]
zippedList = list(zip(names, values))

# 轉回原來的兩個 Lists
# 轉回tuple class
n, v = zip(*zippedList)
print(f'{n = }')
print(f'{type(n) = }')
print(f'{list(n) = }')
print(f'{v = }')
